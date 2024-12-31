from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.question_schema import QuestionDetailResponse, QuestionListResponse, QuestionRequest
from app.db import get_db
from app.services.question_service import (
    create_question_service,
    get_questions_service,
    get_question_by_id_service,
    patch_question_by_id_service,
    delete_question_by_id_service,
)


router = APIRouter()


@router.post("/questions", response_model=QuestionListResponse, status_code=201)
def create_question_endpoint(questions: List[QuestionRequest], db: Session = Depends(get_db)):
    """
    새로운 문제 정보를 생성하는 엔드포인트

    Args:
        question (List[QuestionRequest]): 생성할 문제의 요청 데이터 리스트
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionListResponse: 생성된 문제의 정보
    """
    questions = create_question_service(db, questions)

    return QuestionListResponse(
        message="Questions have been successfully posted.", 
        total=len(questions),
        data=questions
    )


@router.get("/questions", response_model=QuestionListResponse, status_code=200)
def get_question_endpoint(db: Session = Depends(get_db)):
    """
    모든 문제 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionListResponse: 문제 정보 리스트
    """
    questions = get_questions_service(db)

    return QuestionListResponse(
        message="Questions have been successfully posted.", 
        total=len(questions),
        data=questions
    )


@router.get("/questions/{question_id}", response_model=QuestionDetailResponse, status_code=200)
def get_question_by_id_endpoint(question_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 문제 정보를 조회하는 엔드포인트

    Args:
        question_id (int): 조회할 문제의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionResQuestionDetailResponseponse: 조회된 문제의 정보
    """
    question = get_question_by_id_service(db, question_id)

    return QuestionDetailResponse(
        message="Question has been successfully fetched.", 
        data=question
    )
    

@router.patch("/questions/{question_id}", response_model=QuestionDetailResponse, status_code=200)
def patch_question_by_id_endpoint(question_id: int, patch_question: QuestionRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 문제 정보를 수정하는 엔드포인트

    Args:
        question_id (int): 수정할 문제의 고유 ID
        patch_question (QuestionRequest): 수정할 문제의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionDetailResponse: 수정된 문제의 정보
    """
    question = patch_question_by_id_service(db, question_id, patch_question)

    return QuestionDetailResponse(
        message="Question has been successfully patched.", 
        data=question
    )


@router.delete("/questions/{question_id}", response_model=QuestionDetailResponse, status_code=200)
def delete_question_by_id_endpoint(question_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 문제 정보를 삭제하는 엔드포인트

    Args:
        question_id (int): 삭제할 문제의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionResponse: 삭제된 문제의 정보
    """
    question = delete_question_by_id_service(db, question_id)

    return QuestionDetailResponse(
        message="Question has been successfully deleted.", 
        data=question
    )