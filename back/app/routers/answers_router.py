from typing import List, Union
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.answer_schema import AnswerRequest, AnswerResponse
from app.db import get_db
from app.services.answer_service import (
    create_answer_service,
    get_answers_service,
    get_answer_by_id_service,
    patch_answer_by_id_service,
    delete_answer_by_id_service,
)


router = APIRouter()


@router.post("/answers", response_model=List[AnswerResponse])
def create_answer_endpoint(answers: Union[AnswerRequest, List[AnswerRequest]], db: Session = Depends(get_db)):
    """
    새로운 정답 정보를 생성하는 엔드포인트

    Args:
        answers (Union[AnswerRequest, List[AnswerRequest]]): 생성할 정답의 요청 데이터 또는 그 리스트
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        List[AnswerResponse]: 생성된 정답의 정보 리스트
    """
    if isinstance(answers, AnswerRequest):
        answers = [answers]

    created_answers = create_answer_service(db, answers)

    return JSONResponse(
        status_code=201,
        content={
            "message": f"Answers have been successfully posted.",
            "data": {
                "content": [
                    {
                        "question_id": answer.question_id,
                        "answer_text": answer.answer_text,
                        "is_correct": answer.is_correct,
                    }
                    for answer in created_answers
                ]
            },
        },
    )


@router.get("/answers", response_model=List[AnswerResponse])
def get_answer_endpoint(db: Session = Depends(get_db)):
    """
    모든 정답 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        List[AnswerResponse]: 정답 정보 리스트
    """
    answers = get_answers_service(db)

    if not answers:
        raise HTTPException(status_code=404, detail="Answer not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Answers have been successfully fetched.",
            "data": {
                "content": [
                    {
                        "question_id": answer.question_id,
                        "answer_text": answer.answer_text,
                        "is_correct": answer.is_correct,
                    }
                    for answer in answers
                ]
            },
        },
    )


@router.get("/answers/{answer_id}", response_model=AnswerResponse)
def get_answer_by_id_endpoint(answer_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 정답 정보를 조회하는 엔드포인트

    Args:
        answer_id (int): 조회할 정답의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerResponse: 조회된 정답의 정보
    """
    answer = get_answer_by_id_service(db, answer_id)

    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Answer has been successfully fetched.",
            "data": {
                "content": {
                    "question_id": answer.question_id,
                    "answer_text": answer.answer_text,
                    "is_correct": answer.is_correct,
                }
            },
        },
    )


@router.patch("/answers/{answer_id}", response_model=AnswerResponse)
def patch_answer_by_id_endpoint(answer_id: int, patch_answer: AnswerRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 정답 정보를 수정하는 엔드포인트

    Args:
        answer_id (int): 수정할 정답의 고유 ID
        patch_answer (AnswerRequest): 수정할 정답의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerResponse: 수정된 정답의 정보
    """
    patched_answer = patch_answer_by_id_service(db, answer_id, patch_answer)

    if not patched_answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Answer has been successfully patched.",
            "data": {
                "content": {
                    "question_id": patched_answer.question_id,
                    "answer_text": patched_answer.answer_text,
                    "is_correct": patched_answer.is_correct,
                }
            },
        },
    )


@router.delete("/answers/{answer_id}", response_model=AnswerResponse)
def delete_answer_by_id_endpoint(answer_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 정답 정보를 삭제하는 엔드포인트

    Args:
        answer_id (int): 삭제할 정답의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        AnswerResponse: 삭제된 정답의 정보
    """
    deleted_answer = delete_answer_by_id_service(db, answer_id)

    if not deleted_answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Answer has been successfully deleted.",
            "data": {
                "content": {
                    "question_id": deleted_answer.question_id,
                    "answer_text": deleted_answer.answer_text,
                    "is_correct": deleted_answer.is_correct,
                }
            },
        },
    )
