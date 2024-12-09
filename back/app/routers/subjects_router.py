from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.subject_schema import SubjectRequest, SubjectResponse
from app.schemas.exam_schema import ExamResponse
from app.schemas.question_schema import QuestionResponse
from app.db import get_db
from app.services.subject_service import (
    create_subject,
    get_subject,
    get_subject_by_id,
    get_exams_by_subject,
    get_questions_by_subject,
    patch_subject_by_id,
    delete_subject_by_id,
)

router = APIRouter()


@router.post("/subjects", response_model=SubjectResponse)
def create_subject_endpoint(subject: SubjectRequest, db: Session = Depends(get_db)):
    """
    새로운 과목 정보를 생성하는 엔드포인트

    Args:
        subject (SubjectRequest): 생성할 과목의 요청 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        SubjectResponse: 생성된 과목의 정보
    """
    new_subject = create_subject(db, subject)
    return new_subject


@router.get("/subjects", response_model=List[SubjectResponse])
def get_subject_endpoint(
    db: Session = Depends(get_db), 
    name: Optional[str] = Query(None)):
    """
    모든 과목 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체
        name (Optional[str]): 과목 이름 일부를 검색하기 위한 쿼리 파라미터

    Returns:
        List[SubjectResponse]: 과목 정보 리스트
    """
    subjects = get_subject(db, name)
    return subjects


@router.get("/subjects/{subject_id}", response_model=SubjectResponse)
def get_subject_by_id_endpoint(subject_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 조회하는 엔드포인트

    Args:
        subject_id (int): 조회할 과목의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        SubjectResponse: 조회된 과목의 정보
    """
    subject = get_subject_by_id(db, subject_id)
    return subject


@router.get("/subjects/{subject_id}/exams", response_model=List[ExamResponse])
def get_exams_by_subject_endpoint(subject_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목에 포함된 시험 정보를 조회하는 엔드포인트

    Args:
        subject_id (int): 조회할 과목의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        List[ExamResponse]: 조건에 해당하는 시험 정보 리스트
    """
    exams = get_exams_by_subject(db, subject_id)
    return exams


@router.get("/subjects/{subject_id}/questions", response_model=List[QuestionResponse])
def get_questions_by_subject_endpoint(subject_id: int, limit: int, randomize: bool, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목에 포함된 문제 정보를 조회하는 엔드포인트

    Args:
        subject_id (int): 조회할 과목의 고유 ID
        limit (int): 조회할 문제 제한값
        randomize (bool): 랜덤 여부
        db (Session): SQLAlchemy 데이터베이스 세션 객체
    Returns:
        List[ExamResponse]: 조건에 해당하는 시험 정보 리스트

    """
    questions = get_questions_by_subject(db, subject_id, limit, randomize)
    return questions


@router.patch("/subjects/{subject_id}", response_model=SubjectResponse)
def patch_subject_by_id_endpoint(subject_id: int, patch_subject: SubjectRequest, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 수정하는 엔드포인트

    Args:
        subject_id (int): 수정할 과목의 고유 ID
        patch_subject (SubjectRequest): 수정할 과목의 데이터
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        SubjectResponse: 수정된 과목의 정보
    """
    patch_subject = patch_subject_by_id(db, subject_id, patch_subject)
    return patch_subject


@router.delete("/subjects/{subject_id}", response_model=SubjectResponse)
def delete_subject_by_id_endpoint(subject_id: int, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목 정보를 삭제하는 엔드포인트

    Args:
        subject_id (int): 삭제할 과목의 고유 ID
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        SubjectResponse: 삭제된 과목의 정보
    """
    delete_subject = delete_subject_by_id(db, subject_id)
    return delete_subject