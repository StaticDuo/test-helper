from typing import List, Optional
from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from redis import Redis
from app.config import settings
from app.models.user import User
from app.models.exam import Exam
from app.schemas.user_schema import UserJWTResponse, UserResponse
from app.schemas.exam_schema import ExamResponse

from app.repositories.users_repository import get_user_by_email, create_user, get_exam_by_user, get_users, get_user_by_id



# 비밀번호 해싱
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 사용자 생성(회원 가입)
def create_user_service(db: Session, user: User) -> UserResponse:
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=409, detail="Email already exists")

    hashed_password = pwd_context.hash(user.password)
    new_user = User(email=user.email, password=hashed_password)
    created_user = create_user(db, new_user)

    return UserResponse.model_validate(created_user)


# 사용자 로그인
def user_login_service(db: Session, user: User) -> UserJWTResponse:
    authenticated_user = authenticate_user(db, user)
    if not authenticated_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_token(
        data={"sub": authenticated_user.email},
        expires_delta=timedelta(minutes=settings.jwt.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    refresh_token = create_token(
        data={"sub": authenticated_user.email},
        expires_delta=timedelta(days=settings.jwt.REFRESH_TOKEN_EXPIRE_DAYS)
    )

    return UserJWTResponse(
        token_type="bearer",
        access_token=access_token,
        refresh_token=refresh_token,
    )


# 사용자 로그아웃    
def user_logout_service(redis_client: Redis, refresh_token: str):
    ttl = get_token_ttl(refresh_token) 
    redis_key = f"blacklist:refresh-token:{refresh_token}"
    redis_client.set(redis_key, "blacklisted", ex=ttl)


# 사용자 access 토큰 갱신
def user_refresh_service(redis_client: Redis, refresh_token: str) -> UserJWTResponse:

    redis_key = f"blacklist:refresh-token:{refresh_token}"
    if redis_client.get(redis_key):
        raise HTTPException(status_code=401, detail="Invalid or expired refresh token")

    try:
        payload = jwt.decode(refresh_token, settings.jwt.SECRET_KEY, algorithms=[settings.jwt.ALGORITHM])
    except:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid refresh token payload")

    new_access_token = create_token(
        data={"sub": email},
        expires_delta=timedelta(minutes=settings.jwt.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    new_refresh_token = create_token(
        data={"sub": email},
        expires_delta=timedelta(days=settings.jwt.REFRESH_TOKEN_EXPIRE_DAYS)
    )

    ttl = get_token_ttl(refresh_token)
    redis_client.set(redis_key, "blacklisted", ex=ttl)

    return UserJWTResponse(
        token_type="bearer",
        access_token=new_access_token,
        refresh_token=new_refresh_token,
    )


# 토큰의 남은 유효시간 계산
def get_token_ttl(token: str) -> int:
    payload = jwt.decode(token, settings.jwt.SECRET_KEY, algorithms=[settings.jwt.ALGORITHM])
    exp = payload.get("exp")

    if not exp:
        raise HTTPException(status_code=400, detail="Invalid token : 'exp' not found")

    now = datetime.now(timezone.utc)
    exp_time = datetime.fromtimestamp(exp, tz=timezone.utc)
    ttl = (exp_time - now).total_seconds()

    if ttl <= 0:
        raise HTTPException(status_code=400, detail="Token already expired")
    
    return int(ttl)


# 비밀번호 검증
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# 사용자 인증
def authenticate_user(db: Session, user: User) -> Optional[User]:
    db_user = get_user_by_email(db, user.email)
    if not db_user:
        return None

    if not verify_password(user.password, db_user.password):
        return None

    return db_user


# JWT 토큰 생성
def create_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    issue_at = datetime.now(timezone.utc)
    expire = issue_at + expires_delta
    to_encode.update({
        "iat": issue_at,
        "exp": expire
    })
    return jwt.encode(to_encode, settings.jwt.SECRET_KEY, algorithm=settings.jwt.ALGORITHM)


# User 조회 함수
def get_users_service(db: Session, email: Optional[str] = None) -> List[UserResponse]:
    users = get_users(db, email)
    if not users:
        raise HTTPException(status_code=404, detail="User not found")

    return [UserResponse.model_validate(user) for user in users]


# 단일 User 조회 함수
def get_user_by_id_service(db: Session, user_id: int) -> UserResponse:
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return UserResponse.model_validate(user)


# User가 응시한 Exam 조회 함수
def get_exams_by_user_service(db: Session, user_id: int, limit: Optional[int] = 10) -> List[ExamResponse]:
    exams = get_exam_by_user(db, user_id, limit=None)
    if not exams:
        raise HTTPException(status_code=404, detail="Exam not found")

    exams = exams[:limit]        

    return [ExamResponse.model_validate(exam) for exam in exams]
