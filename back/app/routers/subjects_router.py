from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends, Query
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.schemas.subject_schema import SubjectRequest, SubjectResponse
from app.schemas.exam_schema import ExamResponse
from app.schemas.question_schema import QuestionResponse
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
    new_subject = create_subject_service(db, subject)
    return new_subject


@router.get("/subjects", response_model=List[SubjectResponse])
def get_subject_endpoint(db: Session = Depends(get_db), name: Optional[str] = Query(None)):
    """
    검색 조건에 맞는 과목 정보를 가져오는 엔드포인트

    Args:
        db (Session): SQLAlchemy 데이터베이스 세션 객체
        name (Optional[str]): 과목 이름 일부를 검색하기 위한 쿼리 파라미터

    Returns:
        List[SubjectResponse]: 과목 정보 리스트
    """
    subjects = get_subjects_service(db, name)

    if not subjects:
        raise HTTPException(status_code=404, detail="Subject not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Subjects have been successfully fetched.",
            "data": {
                "content": [
                    {
                        "subject_id": subject.subject_id,
                        "name": subject.name,
                        "description": subject.description,
                    }
                    for subject in subjects
                ]
            },
        },
    )


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
    subject = get_subject_by_id_service(db, subject_id)

    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Subject has been successfully fetched.",
            "data": {
                "content": {
                    "subject_id": subject.subject_id,
                    "name": subject.name,
                    "description": subject.description,
                }
            },
        },
    )


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
    exams = get_exams_by_subject_service(db, subject_id)
    if not exams:
        raise HTTPException(status_code=404, detail="Exams not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Subjects have been successfully fetched.",
            "data": {
                "content": [
                    {
                        "exam_id": exam.exam_id,
                        "name": exam.name,
                    }
                    for exam in exams
                ]
            },
        },
    )


@router.get("/subjects/{subject_id}/questions", response_model=List[QuestionResponse])
def get_questions_by_subject_endpoint(subject_id: int, limit: Optional[int] = 10, randomize: Optional[bool] = True, db: Session = Depends(get_db)):
    """
    특정 ID에 해당하는 과목에 포함된 문제 정보를 조회하는 엔드포인트

    Args:
        subject_id (int): 조회할 과목의 고유 ID
        limit (int): 조회할 문제 제한값
        randomize (bool): 랜덤 여부
        db (Session): SQLAlchemy 데이터베이스 세션 객체
    Returns:
        List[QuestionResponse]: 조건에 해당하는 문제 정보 리스트

    """
    questions = get_questions_by_subject_service(db, subject_id, limit, randomize)
    if not questions:
        raise HTTPException(status_code=404, detail="Questions not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Subjects have been successfully fetched.",
            "data": {
                "content": [
                    {
                        "question_id": question.question_id,
                        "exam_id": question.exam_id,
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
    patched_subject = patch_subject_by_id_service(db, subject_id, patch_subject)

    if not patched_subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Subject has been successfully patched.",
            "data": {
                "content": {
                    "subject_id": patched_subject.subject_id,
                    "name": patched_subject.name,
                    "description": patched_subject.description,
                }
            },
        },
    )


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
    deleted_subject = delete_subject_by_id_service(db, subject_id)

    if not deleted_subject:
        raise HTTPException(status_code=404, detail="Subject not found")

    return JSONResponse(
        status_code=200,
        content={
            "message": f"Subject has been successfully deleted.",
            "data": {
                "content": {
                    "subject_id": deleted_subject.subject_id,
                    "name": deleted_subject.name,
                    "description": deleted_subject.description,
                }
            },
        },
    )
