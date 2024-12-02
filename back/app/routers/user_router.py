from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import timedelta
from app.db import get_db
from app.config import settings
from app.schemas.user_schema import UserRequest, UserResponse
from app.services.user_service import create_user, authenticate_user, create_token, get_user, get_user_by_id, verify_and_refresh_token

router = APIRouter()


@router.post("/signup")
def create_user_endpoint(user: UserRequest, db: Session = Depends(get_db)):
    """
    새로운 사용자 정보를 생성하는 엔드포인트

    Args:
        user (UserRequest): 생성할 유저의 요청 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        UserResponse: 생성된 유저의 정보
    """
    new_user = create_user(db, user)
    return new_user


@router.post("/login")
def login_endpoint(user: UserRequest, db: Session = Depends(get_db)):
    """
    사용자 로그인 엔드포인트

    Args:
        user (UserRequest): 로그인할 유저의 요청 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        access token 정보
    """
    user = authenticate_user(db, user.id, user.password)
    if not user:
        return {}

    access_token = create_token(data={"sub": user.id}, expires_delta=timedelta(minutes=settings.jwt.ACCESS_TOKEN_EXPIRE_MINUTES))
    refresh_token = create_token(data={"sub": user.id}, expires_delta=timedelta(days=settings.jwt.REFRESH_TOKEN_EXPIRE_DAYS))
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}


@router.post("/refresh")
def refresh_access_token_endpoint(refresh_token: str, db: Session = Depends(get_db)):
    """
    리프레시 토큰 엔드포인트

    Args:
        refresh_token (str): 리프레시 토큰
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        access token 정보
    """
    new_access_token = verify_and_refresh_token(refresh_token)
    return {"access_token": new_access_token, "token_type": "bearer"}


@router.get("/users", response_model=List[UserResponse])
def get_user_endpoint(db: Session = Depends(get_db)):
    """
    모든 사용자 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        List[UserResponse]: 사용자 정보 리스트
    """
    users = get_user(db)
    return users


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user_by_id_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 사용자 정보를 조회하는 엔드포인트

    Args:
        user_id (int): 조회할 사용자의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        SubjectResponse: 조회된 사용자의 정보
    """
    user = get_user_by_id(db, user_id)
    return user
