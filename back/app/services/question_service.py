from sqlalchemy.orm import Session
from app.models.question import Question
from app.schemas.question_schema import QuestionRequest


# Question 생성 함수
def create_question(db: Session, question_data: QuestionRequest) -> Question:
    new_question = Question(**question_data.model_dump())
    db.add(new_question)
    db.commit()
    db.refresh(new_question)

    return new_question


# Question 조회 함수
def get_question(db: Session) -> Question:
    return db.query(Question).all()


# 단일 Question 조회 함수
def get_question_by_id(db: Session, question_id: int) -> Question:
    return db.query(Question).filter(Question.question_id == question_id).first()


# Question 수정 함수
def patch_question_by_id(db: Session, question_id: int, question_data: QuestionRequest) -> Question:
    patched_question = get_question_by_id(db, question_id)

    if patched_question:
        update_data = question_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(patched_question, key, value)

    db.commit()
    db.refresh(patched_question)

    return patched_question


# Question 삭제 함수
def delete_question_by_id(db: Session, question_id: int) -> Question:
    question = get_question_by_id(db, question_id)
    if question:
        db.delete(question)
        db.commit()

    return question
