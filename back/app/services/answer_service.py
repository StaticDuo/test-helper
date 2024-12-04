from sqlalchemy.orm import Session
from app.models.answer import Answer
from app.schemas.answer_schema import AnswerRequest
from app.repositories.answers_repository import (
    create_answers,
    get_all_answers,
    get_answer_by_id,
    update_answer,
    delete_answer,
)
from typing import List


# Answer 생성 함수
def create_answer_service(db: Session, answer_data: List[AnswerRequest]) -> List[Answer]:
    answers = [Answer(**answer.model_dump()) for answer in answer_data]
    created_answers = create_answers(db, answers)
    if not created_answers:
        return None

    return created_answers


# Answer 조회 함수
def get_answers_service(db: Session) -> List[Answer]:
    answers = get_all_answers(db)
    if not answers:
        return None

    return answers


# 단일 Answer 조회 함수
def get_answer_by_id_service(db: Session, answer_id: int) -> Answer:
    answer = get_answer_by_id(db, answer_id)
    if not answer:
        return None

    return answer


# Answer 수정 함수
def patch_answer_by_id_service(db: Session, answer_id: int, answer_data: AnswerRequest) -> Answer:
    answer = get_answer_by_id(db, answer_id)
    if not answer:
        return None

    update_data = answer_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(answer, key, value)

    return update_answer(db, answer)


# Answer 삭제 함수
def delete_answer_by_id_service(db: Session, answer_id: int) -> Answer:
    answer = get_answer_by_id(db, answer_id)
    if not answer:
        return None
    return delete_answer(db, answer)
