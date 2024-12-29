import random
from typing import List, Optional
from sqlalchemy.orm import Session, joinedload
from app.models.exam import Exam
from app.models.question import Question
from app.schemas.exam_schema import ExamRequest
from app.repositories.exams_repository import (
    create_exams,
    get_exams,
    get_exam_by_id,
    get_questions_by_exam,
    update_exam,
    delete_exam,
)


# Exam 생성 함수
def create_exam_service(db: Session, exam_data: ExamRequest) -> List[Exam]:
    create_exam = []
    for exam in exam_data:
        create_exam.append(Exam(**exam.model_dump()))
    created_exams = create_exams(db, create_exam)
    if not created_exams:
        return None

    return created_exams


# Exam 조회 함수
def get_exams_service(db: Session, name: Optional[str] = None) -> List[Exam]:
    exams = get_exams(db, name)
    if not exams:
        return None

    return exams


# 단일 Exam 조회 함수
def get_exam_by_id_service(db: Session, exam_id: int) -> Exam:
    exam = get_exam_by_id(db, exam_id)
    if not exam:
        return None

    return exam


# Exam에 속한 Questions 조회 함수
def get_questions_by_exam_service(db: Session, exam_id: int, limit: Optional[int] = 10, randomize: Optional[bool] = True) -> Question:
    questions = get_questions_by_exam(db, exam_id)
    if randomize:
        selected_questions = random.sample(questions, min(len(questions), limit))
    else:
        selected_questions = questions[:limit]

    return selected_questions


# Exam 수정 함수
def patch_exam_by_id_service(db: Session, exam_id: int, exam_data: ExamRequest) -> Exam:
    exam = get_exam_by_id(db, exam_id)

    if exam:
        update_data = exam_data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(exam, key, value)

    return update_exam(db, exam)


# Exam 삭제 함수
def delete_exam_by_id_service(db: Session, exam_id: int) -> Exam:
    exam = get_exam_by_id(db, exam_id)
    if not exam:
        return None

    return delete_exam(db, exam)
