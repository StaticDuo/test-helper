from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.subject import Subject
from app.schemas.subject_schema import SubjectRequest, SubjectResponse
from app.schemas.exam_schema import ExamResponse
from app.schemas.question_schema import QuestionResponse
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
def create_subject_service(db: Session, subject_data: List[SubjectRequest]) -> List[SubjectResponse]:
    subjects = [Subject(**subject.model_dump()) for subject in subject_data]
    created_subjects = create_subjects(db, subjects)
    if not created_subjects:
        raise HTTPException(status_code=404, detail="Subject not found")

    return [SubjectResponse.model_validate(subject) for subject in created_subjects]


# Subject 조회 함수
def get_subjects_service(db: Session, name: Optional[str] = None) -> List[SubjectResponse]:
    subjects = get_subjects(db, name)
    if not subjects:
        return HTTPException(status_code=404, detail="Subject not found")

    return [SubjectResponse.model_validate(subject) for subject in subjects]


# 단일 Subject 조회 함수
def get_subject_by_id_service(db: Session, subject_id: int) -> SubjectResponse:
    subject = get_subject_by_id(db, subject_id)
    if not subject:
        return HTTPException(status_code=404, detail="Subject not found")

    return SubjectResponse.model_validate(subject)


# Subject에 속한 Exams 조회 함수
def get_exams_by_subject_service(db: Session, subject_id: int) -> List[ExamResponse]:
    exams = get_exams_by_subject_id(db, subject_id)
    if not exams:
        return HTTPException(status_code=404, detail="Exam not found")

    return [ExamResponse.model_validate(exam) for exam in exams]


# Subject에 속한 Questions 조회 함수
def get_questions_by_subject_service(
    db: Session, subject_id: int, limit: Optional[int] = 10, randomize: Optional[bool] = True
) -> List[QuestionResponse]:
    questions = get_questions_by_subject_id(db, subject_id, limit=None)
    if not questions:
        raise HTTPException(status_code=404, detail="Question not found")

    if randomize:
        questions = random.sample(questions, min(len(questions), limit))
    else:
        questions = questions[:limit]

    return [QuestionResponse.model_validate(question) for question in questions]


# Subject 수정 함수
def patch_subject_by_id_service(db: Session, subject_id: int, subject_data: SubjectRequest) -> SubjectResponse:
    subject = get_subject_by_id(db, subject_id)
    if not subject:
        return HTTPException(status_code=404, detail="Subject not found")

    update_data = subject_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(subject, key, value)

    return SubjectResponse.model_validate(update_subject(db, subject))


# Subject 삭제 함수
def delete_subject_by_id_service(db: Session, subject_id: int) -> SubjectResponse:
    subject = get_subject_by_id(db, subject_id)
    if not subject:
        return HTTPException(status_code=404, detail="Subject not found")

    return SubjectResponse.model_validate(delete_subject(db, subject))
