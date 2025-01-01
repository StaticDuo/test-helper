from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.answer_schema import AnswerDetailResponse, AnswerListResponse, AnswerRequest
from app.db import get_db
from app.services.answer_service import (
    create_answer_service,
    get_answers_service,
    get_answer_by_id_service,
    patch_answer_by_id_service,
    delete_answer_by_id_service,
)


router = APIRouter()


@router.post("/answers", response_model=AnswerListResponse, status_code=201)
def create_answer_endpoint(answers: List[AnswerRequest], db: Session = Depends(get_db)):
    """
    새로운 정답 정보를 생성하는 엔드포인트

    Args:
        answers (AnswerRequest): 생성할 정답의 요청 데이터 리스트
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerListResponse: 생성된 정답의 정보
    """
    answers = create_answer_service(db, answers)

    return AnswerListResponse(
        message="Answers have been successfully posted.", 
        total=len(answers),
        data=answers
    )


@router.get("/answers", response_model=AnswerListResponse, status_code=200)
def get_answer_endpoint(db: Session = Depends(get_db)):
    """
    모든 정답 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerListResponse: 정답 정보 리스트
    """
    answers = get_answers_service(db)

    return AnswerListResponse(
        message="Answers have been successfully posted.", 
        total=len(answers),
        data=answers
    )


@router.get("/answers/{answer_id}", response_model=AnswerDetailResponse)
def get_answer_by_id_endpoint(answer_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 정답 정보를 조회하는 엔드포인트

    Args:
        answer_id (int): 조회할 정답의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerDetailResponse: 조회된 정답의 정보
    """
    answer = get_answer_by_id_service(db, answer_id)

    return AnswerDetailResponse(
        message="Answer has been successfully fetched.", 
        data=answer
    )


@router.patch("/answers/{answer_id}", response_model=AnswerDetailResponse)
def patch_answer_by_id_endpoint(answer_id: int, patch_answer: AnswerRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 정답 정보를 수정하는 엔드포인트

    Args:
        answer_id (int): 수정할 정답의 고유 ID
        patch_answer (AnswerRequest): 수정할 정답의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerDetailResponse: 수정된 정답의 정보
    """
    answer = patch_answer_by_id_service(db, answer_id, patch_answer)

    return AnswerDetailResponse(
        message="Answer has been successfully patched.", 
        data=answer
    )


@router.delete("/answers/{answer_id}", response_model=AnswerDetailResponse)
def delete_answer_by_id_endpoint(answer_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 정답 정보를 삭제하는 엔드포인트

    Args:
        answer_id (int): 삭제할 정답의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerDetailResponse: 삭제된 정답의 정보
    """
    answer = delete_answer_by_id_service(db, answer_id)
    
    return AnswerDetailResponse(
        message="Answer has been successfully deleted.", 
        data=answer
    )
