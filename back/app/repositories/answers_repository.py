from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.answer import Answer
from typing import List


# Answer 생성
def create_answers(db: Session, answers: List[Answer]) -> List[Answer]:
    try:
        db.add_all(answers)
        db.commit()
        for answer in answers:
            db.refresh(answer)
        return answers
    except SQLAlchemyError as e:
        db.rollback()
        raise e


# Answer 조회
def get_all_answers(db: Session) -> List[Answer]:
    return db.query(Answer).all()


# 단일 Answer 조회
def get_answer_by_id(db: Session, answer_id: int) -> Answer:
    return db.query(Answer).filter(Answer.answer_id == answer_id).first()


# Answer 업데이트
def update_answer(db: Session, answer: Answer) -> Answer:
    try:
        db.commit()
        db.refresh(answer)
        return answer
    except SQLAlchemyError as e:
        db.rollback()
        raise e


# Answer 삭제
def delete_answer(db: Session, answer: Answer):
    try:
        db.delete(answer)
        db.commit()
        return answer
    except SQLAlchemyError as e:
        db.rollback()
        raise e
