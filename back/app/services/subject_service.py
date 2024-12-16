from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.subject import Subject
from app.models.exam import Exam
from app.models.question import Question
from app.schemas.subject_schema import SubjectRequest
from app.repositories.subjects_repository import (
    create_subjects,
    get_subjects,
    get_subject_by_id,
    get_exams_by_subject_id,
    get_questions_by_subject_id,
    update_subject,
    delete_subject,
)
import random


# Subject 생성 함수
def create_subject_service(db: Session, subject_data: List[SubjectRequest]) -> List[Subject]:
    subjects = Subject(**subject_data.model_dump())
    created_subjects = create_subjects(db, subjects)
    if not created_subjects:
        return None

    return created_subjects


# Subject 조회 함수
def get_subjects_service(db: Session, name: Optional[str] = None) -> List[Subject]:
    subjects = get_subjects(db, name)
    if not subjects:
        return None

    return subjects


# 단일 Subject 조회 함수
def get_subject_by_id_service(db: Session, subject_id: int) -> Subject:
    subject = get_subject_by_id(db, subject_id)
    if not subject:
        return None

    return subject


# Subject에 속한 Exams 조회 함수
def get_exams_by_subject_service(db: Session, subject_id: int) -> Exam:
    exams = get_exams_by_subject_id(db, subject_id)
    if not exams:
        return None

    return exams


# Subject에 속한 Questions 조회 함수
def get_questions_by_subject_service(db: Session, subject_id: int, limit: Optional[int] = 10, randomize: Optional[bool] = True) -> Question:
    questions = get_questions_by_subject_id(db, subject_id)
    if randomize:
        selected_questions = random.sample(questions, min(len(questions), limit))
    else:
        selected_questions = questions[:limit]

    return selected_questions


# Subject 수정 함수
def patch_subject_by_id_service(db: Session, subject_id: int, subject_data: SubjectRequest) -> Subject:
    subject = get_subject_by_id(db, subject_id)
    if not subject:
        return None

    update_data = subject_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(subject, key, value)

    return update_subject(db, subject)


# Subject 삭제 함수
def delete_subject_by_id_service(db: Session, subject_id: int) -> Subject:
    subject = get_subject_by_id(db, subject_id)
    if not subject:
        return None

    return delete_subject(db, subject)
