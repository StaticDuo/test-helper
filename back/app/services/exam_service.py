from sqlalchemy.orm import Session, joinedload
from app.models.exam import Exam
from app.models.question import Question
from app.schemas.exam_schema import ExamRequest


# Exam 생성 함수
def create_exam(db: Session, exam_data: ExamRequest) -> Exam:
    new_exam = Exam(**exam_data.model_dump())
    db.add(new_exam)
    db.commit()
    db.refresh(new_exam)

    return new_exam


# Exam 조회 함수
def get_exam(db: Session) -> Exam:
    return db.query(Exam).all()


# 단일 Exam 조회 함수
def get_exam_by_id(db: Session, exam_id: int) -> Exam:
    return db.query(Exam).filter(Exam.exam_id == exam_id).first()


# Exam에 속한 Questions 조회 함수
def get_questions_by_exam(db: Session, exam_id: int) -> Question:
    exam = db.query(Exam).options(joinedload(Exam.questions)).filter(Exam.exam_id == exam_id).first()
    return exam.questions


# Exam 수정 함수
def patch_exam_by_id(db: Session, exam_id: int, exam_data: ExamRequest) -> Exam:
    patched_exam = get_exam_by_id(db, exam_id)

    if patched_exam:
        update_data = exam_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(patched_exam, key, value)

    db.commit()
    db.refresh(patched_exam)

    return patched_exam


# Exam 삭제 함수
def delete_exam_by_id(db: Session, exam_id: int) -> Exam:
    exam = get_exam_by_id(db, exam_id)
    if exam:
        db.delete(exam)
        db.commit()

    return exam
