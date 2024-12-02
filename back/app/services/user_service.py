from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.config import settings
from app.models.user import User
from app.schemas.user_schema import UserResponse


# 비밀번호 해싱
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 사용자 생성(회원 가입)
def create_user(db: Session, user: User) -> User:
    existing_user = db.query(User).filter(User.id == user.id).first()
    if existing_user:
        return {}

    hashed_password = pwd_context.hash(user.password)

    new_user = User(id=user.id, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# 비밀번호 검증
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# 사용자 인증
def authenticate_user(db: Session, id: str, password: str):
    user = db.query(User).filter(User.id == id).first()
    if user and pwd_context.verify(password, user.password):
        return user
    return None


# JWT 토큰 생성
def create_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.jwt.SECRET_KEY, algorithm=settings.jwt.ALGORITHM)


def verify_and_refresh_token(refresh_token: str) -> str:
    payload = jwt.decode(refresh_token, settings.jwt.SECRET_KEY, algorithms=[settings.jwt.ALGORITHM])

    user_id: str = payload.get("sub")
    if user_id is None:
        return {}

    new_access_token = create_token({"sub": user_id}, timedelta(minutes=settings.jwt.ACCESS_TOKEN_EXPIRE_MINUTES))

    return new_access_token


# User 조회 함수
def get_user(db: Session) -> User:
    return db.query(User).all()


# User 조회 함수
def get_user_by_id(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.user_id == user_id).first()
