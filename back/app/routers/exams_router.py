from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.exam_schema import ExamRequest, ExamResponse
from app.schemas.question_schema import QuestionResponse
from app.db import get_db
from app.services.exam_service import (
    create_exam_service,
    get_exams_service,
    get_exam_by_id_service,
    get_questions_by_exam_service,
    patch_exam_by_id_service,
    delete_exam_by_id_service,
)


router = APIRouter()


@router.post("/exams", response_model=ExamResponse)
def create_exam_endpoint(exams: List[ExamRequest], db: Session = Depends(get_db)):
    """
    새로운 시험 정보를 생성하는 엔드포인트

    Args:
        exam (List[ExamRequest]): 생성할 시험의 요청 데이터 리스트
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamResponse: 생성된 시험의 정보
    """
    created_exams = create_exam_service(db, exams)

    return JSONResponse(
        status_code=201,
        content={
            "message": f"Exams have been successfully posted.",
            "data": {
                "content": [
                    {
                        "exam_id": exam.exam_id,
                        "subject_id": exam.subject_id,
                        "name": exam.name,
                    }
                    for exam in created_exams
                ]
            },
        },
    )


@router.get("/exams", response_model=List[ExamResponse])
def get_exam_endpoint(db: Session = Depends(get_db), name: Optional[str] = Query(None)):
    """
    모든 시험 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체
        name (Optional[str]): 시험 이름 일부를 검색하기 위한 쿼리 파라미터

    Returns:
        List[ExamResponse]: 시험 정보 리스트
    """
    exams = get_exams_service(db, name)

    if not exams:
        raise HTTPException(status_code=404, detail="Exam not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Exams have been successfully fetched.",
            "data": {
                "content": [
                    {
                        "exam_id": exam.exam_id,
                        "subject_id": exam.subject_id,
                        "name": exam.name,
                    }
                    for exam in exams
                ]
            },
        },
    )


@router.get("/exams/{exam_id}", response_model=ExamResponse)
def get_exam_by_id_endpoint(exam_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 시험 정보를 조회하는 엔드포인트

    Args:
        exam_id (int): 조회할 시험의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamResponse: 조회된 시험의 정보
    """
    exam = get_exam_by_id_service(db, exam_id)

    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Exam has been successfully fetched.",
            "data": {
                "content": {
                    "exam_id": exam.exam_id,
                    "subject_id": exam.subject_id,
                    "name": exam.name,
                }
            },
        },
    )


@router.get("/exams/{exam_id}/questions")
def get_questions_by_exam_endpoint(exam_id: int, limit: Optional[int] = 10, randomize: Optional[bool] = True, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 시험에 포함된 문제 정보를 조회하는 엔드포인트

    Args:
        exam_id (int): 조회할 시험의 고유 ID
        limit (int): 조회할 문제 제한값
        randomize (bool): 랜덤 여부
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        List[ExamResponse]: 조건에 해당하는 문제 정보 리스트

    """
    questions = get_questions_by_exam_service(db, exam_id, limit, randomize)

    if not questions:
        raise HTTPException(status_code=404, detail="Question not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Questions have been successfully fetched.",
            "data": {
                "content": [
                    {
                        "question_id": question.question_id,
                        "question_number": question.question_number,
                        "question_text": question.question_text,
                        "question_type": question.question_type,
                        "answers": [
                            {
                                "answer_id": answer.answer_id,
                                "question_id": answer.question_id,
                                "answer_text": answer.answer_text,
                            }
                            for answer in question.answers
                        ],
                    }
                    for question in questions
                ]
            },
        },
    )


@router.patch("/exams/{exam_id}", response_model=ExamResponse)
def patch_exam_by_id_endpoint(exam_id: int, patch_exam: ExamRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 시험 정보를 수정하는 엔드포인트

    Args:
        exam_id (int): 수정할 시험의 고유 ID
        patch_exam (ExamRequest): 수정할 시험의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamResponse: 수정된 시험의 정보
    """
    patched_exam = patch_exam_by_id_service(db, exam_id, patch_exam)

    if not patched_exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Exam has been successfully patched.",
            "data": {
                "content": {
                    "exam_id": patched_exam.exam_id,
                    "subject_id": patched_exam.subject_id,
                    "name": patched_exam.name,
                }
            },
        },
    )


@router.delete("/exams/{exam_id}", response_model=ExamResponse)
def delete_exam_by_id_endpoint(exam_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 시험 정보를 삭제하는 엔드포인트

    Args:
        exam_id (int): 삭제할 시험의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamResponse: 삭제된 시험의 정보
    """
    deleted_exam = delete_exam_by_id_service(db, exam_id)

    if not deleted_exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Exam has been successfully deleted.",
            "data": {
                "content": {
                    "exam_id": deleted_exam.exam_id,
                    "subject_id": deleted_exam.subject_id,
                    "name": deleted_exam.name,
                }
            },
        },
    )
