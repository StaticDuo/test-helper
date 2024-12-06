from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.question import Question
from typing import List


# Question 생성
def create_questions(db: Session, questions: List[Question]) -> List[Question]:
    try:
        db.add_all(questions)
        db.commit()
        for question in questions:
            db.refresh(question)
        return questions
    except SQLAlchemyError as e:
        db.rollback()
        raise e


# Question 조회
def get_all_questions(db: Session) -> List[Question]:
    return db.query(Question).all()


# 단일 Question 조회
def get_question_by_id(db: Session, question_id: int) -> Question:
    return db.query(Question).filter(Question.question_id == question_id).first()


# Question 업데이트
def update_question(db: Session, question: Question) -> Question:
    try:
        db.commit()
        db.refresh(question)
        return question
    except SQLAlchemyError as e:
        db.rollback()
        raise e


# Question 삭제
def delete_question(db: Session, question: Question):
    try:
        db.delete(question)
        db.commit()
        return question
    except SQLAlchemyError as e:
        db.rollback()
        raise e
