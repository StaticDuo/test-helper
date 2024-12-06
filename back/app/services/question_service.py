from sqlalchemy.orm import Session
from app.models.question import Question
from app.schemas.question_schema import QuestionRequest
from app.repositories.questions_repository import (
    create_questions,
    get_all_questions,
    get_question_by_id,
    update_question,
    delete_question,
)
from typing import List


# Question 생성 함수
def create_question_service(db: Session, question_data: List[QuestionRequest]) -> List[Question]:
    questions = Question(**question_data.model_dump())
    created_questions = create_questions(db, questions)
    if not created_questions:
        return None

    return created_questions


# Question 조회 함수
def get_questions_service(db: Session) -> List[Question]:
    questions = get_all_questions(db)
    if not questions:
        return None

    return questions


# 단일 Question 조회 함수
def get_question_by_id_service(db: Session, question_id: int) -> Question:
    question = get_question_by_id(db, question_id)
    if not question:
        return None

    return question


# Question 수정 함수
def patch_question_by_id_service(db: Session, question_id: int, question_data: QuestionRequest) -> Question:
    question = get_question_by_id(db, question_id)
    if not question:
        return None

    update_data = question_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(question, key, value)

    return update_question(db, question)


# question 삭제 함수
def delete_question_by_id_service(db: Session, question_id: int) -> Question:
    question = get_question_by_id(db, question_id)
    if not question:
        return None
    return delete_question(db, question)
