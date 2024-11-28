from sqlalchemy.orm import Session
from app.models.answer import Answer
from app.schemas.answer_schema import AnswerRequest


# Answer 생성 함수
def create_answer(db: Session, answer_data: AnswerRequest) -> Answer:
    new_answer = Answer(**answer_data.model_dump())
    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)

    return new_answer


# Answer 조회 함수
def get_answer(db: Session) -> Answer:
    return db.query(Answer).all()


# 단일 Answer 조회 함수
def get_answer_by_id(db: Session, answer_id: int) -> Answer:
    return db.query(Answer).filter(Answer.answer_id == answer_id).first()


def patch_answer_by_id(db: Session, answer_id: int, answer_data: AnswerRequest) -> Answer:
    patched_answer = get_answer_by_id(db, answer_id)

    if patched_answer:
        update_data = answer_data.dict(exclude_unset=True)
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
