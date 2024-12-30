from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.answer import Answer
from app.schemas.answer_schema import AnswerRequest, AnswerResponse
from app.repositories.answers_repository import (
    create_answers,
    get_answers,
    get_answer_by_id,
    update_answer,
    delete_answer,
)


# Answer 생성 함수
def create_answer_service(db: Session, answer_data: List[AnswerRequest]) -> List[AnswerResponse]:
    answers = [Answer(**answer.model_dump()) for answer in answer_data]
    created_answers = create_answers(db, answers)
    if not created_answers:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    return [AnswerResponse.model_validate(answer) for answer in created_answers]


# Answer 조회 함수
def get_answers_service(db: Session) -> List[AnswerResponse]:
    answers = get_answers(db)
    if not answers:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    return [AnswerResponse.model_validate(answer) for answer in answers]


# 단일 Answer 조회 함수
def get_answer_by_id_service(db: Session, answer_id: int) -> AnswerResponse:
    answer = get_answer_by_id(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    return AnswerResponse.model_validate(answer)


# Answer 수정 함수
def patch_answer_by_id_service(db: Session, answer_id: int, answer_data: AnswerRequest) -> AnswerResponse:
    answer = get_answer_by_id(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")

    update_data = answer_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(answer, key, value)

    return AnswerResponse.model_validate(update_answer(db, answer))


# Answer 삭제 함수
def delete_answer_by_id_service(db: Session, answer_id: int) -> AnswerResponse:
    answer = get_answer_by_id(db, answer_id)
    if not answer:
        raise HTTPException(status_code=404, detail="Answer not found")
    
    return AnswerResponse.model_validate(delete_answer(db, answer))
