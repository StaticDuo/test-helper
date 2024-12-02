from sqlalchemy.orm import Session
from app.models.answer import Answer
from app.schemas.answer_schema import AnswerRequest
from typing import List


# Answer 생성 함수
def create_answer(db: Session, answer_data: List[AnswerRequest]) -> List[Answer]:
    answers = [Answer(**answer.model_dump()) for answer in answer_data]

    db.add_all(answers)
    db.commit()

    for answer in answers:
        db.refresh(answer)

    return answers


# Answer 조회 함수
def get_answer(db: Session) -> Answer:
    return db.query(Answer).all()


# 단일 Answer 조회 함수
def get_answer_by_id(db: Session, answer_id: int) -> Answer:
    return db.query(Answer).filter(Answer.answer_id == answer_id).first()


# Answer 수정 함수
def patch_answer_by_id(db: Session, answer_id: int, answer_data: AnswerRequest) -> Answer:
    patched_answer = get_answer_by_id(db, answer_id)

    if patched_answer:
        update_data = answer_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(patched_answer, key, value)

    db.commit()
    db.refresh(patched_answer)

    return patched_answer


# Answer 삭제 함수
def delete_answer_by_id(db: Session, answer_id: int) -> Answer:
    answer = get_answer_by_id(db, answer_id)
    if answer:
        db.delete(answer)
        db.commit()

    return answer
