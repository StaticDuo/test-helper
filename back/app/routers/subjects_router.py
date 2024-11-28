from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.subject_schema import SubjectRequest, SubjectResponse
from app.db import get_db
from app.services.subject_service import (
    create_subject,
    get_subject,
    get_subject_by_id,
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
def get_subject_endpoint(db: Session = Depends(get_db)):
    """
    모든 과목 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체

    Returns:
        List[SubjectResponse]: 과목 정보 리스트
    """
    subjects = get_subject(db)
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
