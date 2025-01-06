from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from app.models.question import Question
from app.models.subject import Subject
from app.models.exam import Exam
from app.schemas.question_schema import QuestionResponse
from typing import List, Optional


# Subject 생성
def create_subjects(db: Session, subjects: List[Subject]) -> List[Subject]:
    try:
        db.add_all(subjects)
        db.commit()
        for subject in subjects:
            db.refresh(subject)
        return subjects
    except SQLAlchemyError:
        db.rollback()
        raise


# Subject 조회
def get_subjects(db: Session, name: Optional[str] = None) -> List[Subject]:
    query = db.query(Subject)
    if name:
        query = query.filter(Subject.name.ilike(f"%{name}%"))

    return query.all()


# 단일 Subject 조회
def get_subject_by_id(db: Session, subject_id: int) -> Subject:
    return db.query(Subject).filter(Subject.subject_id == subject_id).first()


# Subject에 속한 Exams 조회
def get_exams_by_subject_id(db: Session, subject_id: int) -> List[Exam]:
    return db.query(Exam).filter(Exam.subject_id == subject_id).all()


# Subject에 속한 Questions 조회
def get_questions_by_subject_id(db: Session, subject_id: int, limit: Optional[int]) -> List[QuestionResponse]:
    query = db.query(Question).join(Question.exam).options(joinedload(Question.answers)).filter(Exam.subject_id == subject_id)
    if limit:
        query = query.limit(limit)
    return query.all()


# Subject 업데이트
def update_subject(db: Session, subject: Subject) -> Subject:
    try:
        db.commit()
        db.refresh(subject)
        return subject
    except SQLAlchemyError:
        db.rollback()
        raise


# Subject 삭제
def delete_subject(db: Session, subject: Subject):
    try:
        db.delete(subject)
        db.commit()
        return subject
    except SQLAlchemyError:
        db.rollback()
        raise
