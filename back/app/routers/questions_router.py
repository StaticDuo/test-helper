from typing import List, Union
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.question_schema import QuestionRequest, QuestionResponse
from app.db import get_db
from app.services.question_service import (
    create_question_service,
    get_questions_service,
    get_question_by_id_service,
    patch_question_by_id_service,
    delete_question_by_id_service,
)


router = APIRouter()


@router.post("/questions", response_model=QuestionResponse)
def create_question_endpoint(questions: QuestionRequest, db: Session = Depends(get_db)):
    """
    새로운 문제 정보를 생성하는 엔드포인트

    Args:
        question (QuestionRequest): 생성할 문제의 요청 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionResponse: 생성된 문제의 정보
    """
    if isinstance(questions, QuestionRequest):
        questions = [questions]

    created_questions = create_question_service(db, questions)

    return JSONResponse(
        status_code=201,
        content={
            "message": f"Questions have been successfully posted.",
            "data": {
                "content": [
                    {
                        "exam_id": question.exam_id,
                        "question_number": question.question_number,
                        "question_text": question.question_text,
                        "question_type": question.question_type,
                    }
                    for question in created_questions
                ]
            },
        },
    )


@router.get("/questions", response_model=List[QuestionResponse])
def get_question_endpoint(db: Session = Depends(get_db)):
    """
    모든 문제 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        List[QuestionResponse]: 문제 정보 리스트
    """
    questions = get_questions_service(db)

    if not questions:
        raise HTTPException(status_code=404, detail="Question not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Questions have been successfully fetched.",
            "data": {
                "content": [
                    {
                        "exam_id": question.exam_id,
                        "question_number": question.question_number,
                        "question_text": question.question_text,
                        "question_type": question.question_type,
                    }
                    for question in questions
                ]
            },
        },
    )


@router.get("/questions/{question_id}", response_model=QuestionResponse)
def get_question_by_id_endpoint(question_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 문제 정보를 조회하는 엔드포인트

    Args:
        question_id (int): 조회할 문제의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionResponse: 조회된 문제의 정보
    """
    question = get_question_by_id_service(db, question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Question have been successfully fetched.",
            "data": {
                "content": {
                    "exam_id": question.exam_id,
                    "question_number": question.question_number,
                    "question_text": question.question_text,
                    "question_type": question.question_type,
                }
            },
        },
    )


@router.patch("/questions/{question_id}", response_model=QuestionResponse)
def patch_question_by_id_endpoint(question_id: int, patch_question: QuestionRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 문제 정보를 수정하는 엔드포인트

    Args:
        question_id (int): 수정할 문제의 고유 ID
        patch_question (QuestionRequest): 수정할 문제의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionResponse: 수정된 문제의 정보
    """
    patched_question = patch_question_by_id_service(db, question_id, patch_question)

    if not patched_question:
        raise HTTPException(status_code=404, detail="Question not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Question has been successfully patched.",
            "data": {
                "content": {
                    "exam_id": patched_question.exam_id,
                    "question_number": patched_question.question_number,
                    "question_text": patched_question.question_text,
                    "question_type": patched_question.question_type,
                }
            },
        },
    )


@router.delete("/questions/{question_id}", response_model=QuestionResponse)
def delete_question_by_id_endpoint(question_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 문제 정보를 삭제하는 엔드포인트

    Args:
        question_id (int): 삭제할 문제의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionResponse: 삭제된 문제의 정보
    """
    deleted_question = delete_question_by_id_service(db, question_id)

    if not deleted_question:
        raise HTTPException(status_code=404, detail="Question not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Question has been successfully deleted.",
            "data": {
                "content": {
                    "exam_id": deleted_question.exam_id,
                    "question_number": deleted_question.question_number,
                    "question_text": deleted_question.question_text,
                    "question_type": deleted_question.question_type,
                }
            },
        },
    )
