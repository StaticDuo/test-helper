from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.exam_schema import ExamDetailResponse, ExamListResponse, ExamRequest
from app.schemas.question_schema import QuestionListResponse
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


@router.post("/exams", response_model=ExamListResponse, status_code=201)
def create_exam_endpoint(exams: List[ExamRequest], db: Session = Depends(get_db)):
    """
    새로운 시험 정보를 생성하는 엔드포인트

    Args:
        exam (List[ExamRequest]): 생성할 시험의 요청 데이터 리스트
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamListResponse: 생성된 시험의 정보
    """
    exams = create_exam_service(db, exams)

    return ExamListResponse(
        message="Exams have been successfully posted.", 
        total=len(exams),
        data=exams
    )


@router.get("/exams", response_model=ExamListResponse, status_code=200)
def get_exam_endpoint(db: Session = Depends(get_db), name: Optional[str] = Query(None)):
    """
    모든 시험 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체
        name (Optional[str]): 시험 이름 일부를 검색하기 위한 쿼리 파라미터

    Returns:
        ExamListResponse: 시험 정보 리스트
    """
    exams = get_exams_service(db, name)

    return ExamListResponse(
        message="Exams have been successfully fetched.", 
        total=len(exams), 
        data=exams
    )


@router.get("/exams/{exam_id}", response_model=ExamDetailResponse, status_code=200)
def get_exam_by_id_endpoint(exam_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 시험 정보를 조회하는 엔드포인트

    Args:
        exam_id (int): 조회할 시험의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamDetailResponse: 조회된 시험의 정보
    """
    exam = get_exam_by_id_service(db, exam_id)

    return ExamDetailResponse(
        message="Exam has been successfully fetched.", 
        data=exam
    )


@router.get("/exams/{exam_id}/questions", response_model=QuestionListResponse, status_code=200)
def get_questions_by_exam_endpoint(exam_id: int, limit: Optional[int] = 10, randomize: Optional[bool] = True, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 시험에 포함된 문제 정보를 조회하는 엔드포인트

    Args:
        exam_id (int): 조회할 시험의 고유 ID
        limit (int): 조회할 문제 제한값
        randomize (bool): 랜덤 여부
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        QuestionListResponse: 조건에 해당하는 문제 정보 리스트

    """
    questions = get_questions_by_exam_service(db, exam_id, limit, randomize)

    return QuestionListResponse(
        message="Questions have been successfully fetched.", 
        total=len(questions), 
        data=questions
    )


@router.patch("/exams/{exam_id}", response_model=ExamDetailResponse, status_code=200)
def patch_exam_by_id_endpoint(exam_id: int, patch_exam: ExamRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 시험 정보를 수정하는 엔드포인트

    Args:
        exam_id (int): 수정할 시험의 고유 ID
        patch_exam (ExamRequest): 수정할 시험의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamDetailResponse: 수정된 시험의 정보
    """
    exam = patch_exam_by_id_service(db, exam_id, patch_exam)

    return ExamDetailResponse(
        message="Exam has been successfully patched.", 
        data=exam
    )


@router.delete("/exams/{exam_id}", response_model=ExamDetailResponse, status_code=200)
def delete_exam_by_id_endpoint(exam_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 시험 정보를 삭제하는 엔드포인트

    Args:
        exam_id (int): 삭제할 시험의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamDetailResponse: 삭제된 시험의 정보
    """
    exam = delete_exam_by_id_service(db, exam_id)

    return ExamDetailResponse(
        message="Exam has been successfully deleted.", 
        data=exam
    )
    