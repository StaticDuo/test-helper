from typing import Optional
from sqlalchemy.orm import Session, joinedload
from app.models.subject import Subject
from app.models.exam import Exam
from app.models.question import Question
from app.schemas.subject_schema import SubjectRequest
import random


# Subject 생성 함수
def create_subject(db: Session, subject_data: SubjectRequest) -> Subject:
    new_subject = Subject(**subject_data.model_dump())
    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)

    return new_subject


# Subject 조회 함수
def get_subject(db: Session, name: Optional[str] = None) -> Subject:
    query = db.query(Subject)

    if name:
        query = query.filter(Subject.name.ilike(f"%{name}%"))
        
    return query.all()


# 단일 Subject 조회 함수
def get_subject_by_id(db: Session, subject_id: int) -> Subject:
    return db.query(Subject).filter(Subject.subject_id == subject_id).first()


# Subject에 속한 Exams 조회 함수
def get_exams_by_subject(db: Session, subject_id: int) -> Exam:
    subject = db.query(Subject).options(joinedload(Subject.exams)).filter(Subject.subject_id == subject_id).first()
    return subject.exams


# Subject에 속한 Questions 조회 함수
def get_questions_by_subject(db: Session, subject_id: int, limit: int, randomize: bool) -> Question:
    exams = get_exams_by_subject(db, subject_id)

    all_questions = list()
    for exam in exams:
        all_questions.extend(exam.questions)

    if randomize:
        selected_questions = random.sample(all_questions, min(len(all_questions), limit))
    else:
        selected_questions = all_questions[:limit]

    return selected_questions


# Subject 수정 함수
def patch_subject_by_id(db: Session, subject_id: int, subject_data: SubjectRequest) -> Subject:
    patched_subject = get_subject_by_id(db, subject_id)

    if patched_subject:
        update_data = subject_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(patched_subject, key, value)

    db.commit()
    db.refresh(patched_subject)

    return patched_subject


# Subject 삭제 함수
def delete_subject_by_id(db: Session, subject_id: int) -> Subject:
    subject = get_subject_by_id(db, subject_id)
    if subject:
        db.delete(subject)
        db.commit()

    return subject
