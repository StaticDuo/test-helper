from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from app.models.question import Question
from app.models.exam import Exam
from typing import List, Optional


# Exam 생성
def create_exams(db: Session, exams: List[Exam]) -> List[Exam]:
    try:
        db.add_all(exams)
        db.commit()
        for exam in exams:
            db.refresh(exam)
        return exams
    except SQLAlchemyError:
        db.rollback()
        raise


# Exam 조회
def get_exams(db: Session, name: Optional[str] = None) -> List[Exam]:
    query = db.query(Exam)

    if name:
        query = query.filter(Exam.name.ilike(f"%{name}%"))

    return query.all()


# 단일 Exam 조회
def get_exam_by_id(db: Session, exam_id: int) -> Exam:
    return db.query(Exam).filter(Exam.exam_id == exam_id).first()


# Exam에 속한 Questions 조회
def get_questions_by_exam(db: Session, exam_id: int, limit: Optional[int]) -> List[Question]:
    query = db.query(Question).options(joinedload(Question.answers)).filter(Question.exam_id == exam_id)

    if limit:
        query = query.limit(limit)

    print(query)

    return query.all()


# Exam 업데이트
def update_exam(db: Session, exam: Exam) -> Exam:
    try:
        db.commit()
        db.refresh(exam)
        return exam
    except SQLAlchemyError:
        db.rollback()
        raise


# Exam 삭제
def delete_exam(db: Session, exam: Exam):
    try:
        db.delete(exam)
        db.commit()
        return exam
    except SQLAlchemyError:
        db.rollback()
        raise
