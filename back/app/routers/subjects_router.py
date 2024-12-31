from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.subject_schema import SubjectDetailResponse, SubjectListResponse, SubjectRequest
from app.schemas.exam_schema import ExamListResponse
from app.schemas.question_schema import QuestionListResponse
from app.db import get_db
from app.services.subject_service import (
    create_subject_service,
    get_subjects_service,
    get_subject_by_id_service,
    get_exams_by_subject_service,
    get_questions_by_subject_service,
    patch_subject_by_id_service,
    delete_subject_by_id_service,
)


router = APIRouter()


@router.post("/subjects", response_model=SubjectListResponse, status_code=201)
def create_subject_endpoint(subjects: List[SubjectRequest], db: Session = Depends(get_db)):
    """
    새로운 과목 정보를 생성하는 엔드포인트

    Args:
        subjects (List[SubjectRequest]): 생성할 과목의 요청 데이터 리스트
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        SubjectListResponse: 생성된 과목의 정보
    """
    subjects = create_subject_service(db, subjects)

    return SubjectListResponse(
        message="Subjects have been successfully posted.", 
        total=len(subjects),
        data=subjects
    )


@router.get("/subjects", response_model=SubjectListResponse, status_code=200)
def get_subject_endpoint(db: Session = Depends(get_db), name: Optional[str] = Query(None)):
    """
    검색 조건에 맞는 과목 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체
        name (Optional[str]): 과목 이름 일부를 검색하기 위한 쿼리 파라미터

    Returns:
        SubjectListResponse: 과목 정보 리스트
    """
    subjects = get_subjects_service(db, name)

    return SubjectListResponse(
        message="Subjects have been successfully posted.", 
        total=len(subjects),
        data=subjects
    )


@router.get("/subjects/{subject_id}", response_model=SubjectDetailResponse, status_code=200)
def get_subject_by_id_endpoint(subject_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 조회하는 엔드포인트

    Args:
        subject_id (int): 조회할 과목의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        SubjectDetailResponse: 조회된 과목의 정보
    """
    subject = get_subject_by_id_service(db, subject_id)

    return SubjectDetailResponse(
        message="Subject has been successfully fetched.", 
        data=subject
    )


@router.get("/subjects/{subject_id}/exams", response_model=ExamListResponse, status_code=200)
def get_exams_by_subject_endpoint(subject_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목에 포함된 시험 정보를 조회하는 엔드포인트

    Args:
        subject_id (int): 조회할 과목의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        ExamListResponse: 조건에 해당하는 시험 정보 리스트
    """
    exams = get_exams_by_subject_service(db, subject_id)

    return ExamListResponse(
        message="Exams have been successfully fetched.", 
        total=len(exams), 
        data=exams
    )


@router.get("/subjects/{subject_id}/questions", response_model=QuestionListResponse, status_code=200)
def get_questions_by_subject_endpoint(subject_id: int, limit: Optional[int] = 10, randomize: Optional[bool] = True, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목에 포함된 문제 정보를 조회하는 엔드포인트

    Args:
        subject_id (int): 조회할 과목의 고유 ID
        limit (int): 조회할 문제 제한값
        randomize (bool): 랜덤 여부
        db (Session): SQLAlchemy 데이터베이스 세션 객체
        
    Returns:
        QuestionListResponse: 조건에 해당하는 문제 정보 리스트

    """
    questions = get_questions_by_subject_service(db, subject_id, limit, randomize)

    return QuestionListResponse(
        message="Questions have been successfully fetched.", 
        total=len(questions), 
        data=questions
    )


@router.patch("/subjects/{subject_id}", response_model=SubjectDetailResponse)
def patch_subject_by_id_endpoint(subject_id: int, patch_subject: SubjectRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 수정하는 엔드포인트

    Args:
        subject_id (int): 수정할 과목의 고유 ID
        patch_subject (SubjectRequest): 수정할 과목의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        SubjectDetailResponse: 수정된 과목의 정보
    """
    subject = patch_subject_by_id_service(db, subject_id, patch_subject)

    return SubjectDetailResponse(
        message="Subject has been successfully patched.", 
        data=subject
    )


@router.delete("/subjects/{subject_id}", response_model=SubjectDetailResponse)
def delete_subject_by_id_endpoint(subject_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 삭제하는 엔드포인트

    Args:
        subject_id (int): 삭제할 과목의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        SubjectDetailResponse: 삭제된 과목의 정보
    """
    subject = delete_subject_by_id_service(db, subject_id)
    
    return SubjectDetailResponse(
        message="Subject has been successfully deleted.", 
        data=subject
    )
    