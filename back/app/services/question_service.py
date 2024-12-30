from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.question import Question
from app.schemas.question_schema import QuestionRequest, QuestionResponse
from app.repositories.questions_repository import (
    create_questions,
    get_questions,
    get_question_by_id,
    update_question,
    delete_question,
)


# Question 생성 함수
def create_question_service(db: Session, question_data: List[QuestionRequest]) -> List[QuestionResponse]:
    questions = [Question(**question.model_dump()) for question in question_data]
    created_questions = create_questions(db, questions)
    if not created_questions:
        raise HTTPException(status_code=404, detail="Question not found")

    return [QuestionResponse.model_validate(question) for question in created_questions]


# Question 조회 함수
def get_questions_service(db: Session) -> List[QuestionResponse]:
    questions = get_questions(db)
    if not questions:
        raise HTTPException(status_code=404, detail="Question not found")

    return [QuestionResponse.model_validate(question) for question in questions]


# 단일 Question 조회 함수
def get_question_by_id_service(db: Session, question_id: int) -> QuestionResponse:
    question = get_question_by_id(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return QuestionResponse.model_validate(question)


# Question 수정 함수
def patch_question_by_id_service(db: Session, question_id: int, question_data: QuestionRequest) -> QuestionResponse:
    question = get_question_by_id(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    update_data = question_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(question, key, value)

    return QuestionResponse.model_validate(update_question(db, question))


# question 삭제 함수
def delete_question_by_id_service(db: Session, question_id: int) -> QuestionResponse:
    question = get_question_by_id(db, question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return QuestionResponse.model_validate(delete_question(db, question))