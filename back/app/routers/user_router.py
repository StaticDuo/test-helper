from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.db import get_db, get_redis_client
from app.schemas.exam_schema import ExamListResponse
from app.schemas.user_schema import UserDetailResponse, UserJWTDetailResponse, UserListResponse, UserRequest, UserResponse
from app.services.user_service import (
    create_user_service,
    user_login_service,
    user_logout_service,
    user_refresh_service,
    get_users_service,
    get_user_by_id_service,
    get_exams_by_user_service,
)
import redis


public_router = APIRouter()
protected_router = APIRouter()

@public_router.post("/signup", response_model=UserDetailResponse, status_code=201)
def create_user_endpoint(user: UserRequest, db: Session = Depends(get_db)):
    """
    새로운 사용자 정보를 생성하는 엔드포인트

    Args:
        user (UserRequest): 생성할 유저의 요청 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        UserResponse: 생성된 유저의 정보
    """
    user = create_user_service(db, user)
    return UserDetailResponse(
        message="Signup success",
        data=user
    )


@public_router.post("/login", response_model=UserJWTDetailResponse, status_code=200)
def login_endpoint(user: UserRequest, db: Session = Depends(get_db)):
    """
    사용자 로그인 엔드포인트

    Args:
        user (UserRequest): 로그인할 유저의 요청 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        UserJWTDetailResponse: JWT 토큰 정보
    """
    user_jwt = user_login_service(db, user)

    return UserJWTDetailResponse(
        message="Login success",
        data=user_jwt
    )


@public_router.post("/logout", status_code=200)
def logout_endpoint(refresh_token: str, redis_client: redis = Depends(get_redis_client)):
    """
    사용자 로그아웃 엔드포인트

    Args:
        user (UserRequest): 로그아웃할 유저의 요청 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
    """
    user_logout_service(redis_client, refresh_token)

    return {"message": "Logout Success"}


@public_router.post("/refresh", response_model=UserJWTDetailResponse, status_code=200)
def refresh_access_token_endpoint(refresh_token: str, redis_client: redis = Depends(get_redis_client)):
    """
    리프레시 토큰 엔드포인트

    Args:
        refresh_token (str): 리프레시 토큰
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        access token 정보
    """
    token_data = user_refresh_service(redis_client, refresh_token)
    
    return UserJWTDetailResponse(
        message="Refresh token success",
        data=token_data   
    )


@protected_router.get("/users", response_model=UserListResponse, status_code=200)
def get_user_endpoint(db: Session = Depends(get_db), email: Optional[str] = Query(None)):
    """
    모든 사용자 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체
        email (Optional[str]): email 일부를 검색하기 위한 쿼리 파라미터

    Returns:
        UserListResponse: 사용자 정보 리스트
    """
    users = get_users_service(db, email)
    
    return UserListResponse(
        message="Users have been successfully fetched.",
        total=len(users),
        data=users
    )


@protected_router.get("/users/{user_id}", response_model=UserDetailResponse, status_code=200)
def get_user_by_id_endpoint(user_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 사용자 정보를 조회하는 엔드포인트

    Args:
        user_id (int): 조회할 사용자의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        UserDetailResponse: 조회된 사용자의 정보
    """
    user = get_user_by_id_service(db, user_id)

    return UserDetailResponse(
        message="User has been successfully fetched.",
        data=user
    )
    

@protected_router.get("/users/{user_id}/exams", response_model=ExamListResponse, status_code=200)
def get_exams_by_user_id_endpoint(user_id: int, limit: Optional[int] = 10, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 사용자가 응시한 시험 정보를 조회하는 엔드포인트

    Args:
        user_id (int): 응시한 시험 정보를 조회할 사용자의 고유 ID
        limit (int): 조회할 문제 제한값
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamListResponse: 조건에 해당하는 시험 정보 리스트
    """
    exams = get_exams_by_user_service(db, user_id, limit)

    return ExamListResponse(
        message="Exams have been successfully fetched.", 
        total=len(exams),
        data=exams
    )
