from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.subject import Subject
from typing import List


# Subject 생성
def create_Subjects(db: Session, Subjects: List[Subject]) -> List[Subject]:
    try:
        db.add_all(Subjects)
        db.commit()
        for Subject in Subjects:
            db.refresh(Subject)
        return Subjects
    except SQLAlchemyError as e:
        db.rollback()
        raise e


# Subject 조회
def get_all_Subjects(db: Session) -> List[Subject]:
    return db.query(Subject).all()


# 단일 Subject 조회
def get_Subject_by_id(db: Session, Subject_id: int) -> Subject:
    return db.query(Subject).filter(Subject.Subject_id == Subject_id).first()


# Subject 업데이트
def update_Subject(db: Session, Subject: Subject) -> Subject:
    try:
        db.commit()
        db.refresh(Subject)
        return Subject
    except SQLAlchemyError as e:
        db.rollback()
        raise e


# Subject 삭제
def delete_Subject(db: Session, Subject: Subject):
    try:
        db.delete(Subject)
        db.commit()
        return Subject
    except SQLAlchemyError as e:
        db.rollback()
        raise e
