import random
from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload
from app.models.exam import Exam
from app.schemas.exam_schema import ExamRequest, ExamResponse
from app.schemas.question_schema import QuestionResponse
from app.repositories.exams_repository import (
    create_exams,
    get_exams,
    get_exam_by_id,
    get_questions_by_exam,
    update_exam,
    delete_exam,
)


# Exam 생성 함수
def create_exam_service(db: Session, exam_data: List[ExamRequest]) -> List[ExamResponse]:
    exams = [Exam(**exam.model_dump()) for exam in exam_data]
    created_exams = create_exams(db, exams)
    if not created_exams:
        raise HTTPException(status_code=404, detail="Exam not found")

    return [ExamResponse.model_validate(exam) for exam in created_exams]


# Exam 조회 함수
def get_exams_service(db: Session, name: Optional[str] = None) -> List[ExamResponse]:
    exams = get_exams(db, name)
    if not exams:
        raise HTTPException(status_code=404, detail="Exam not found")

    return [ExamResponse.model_validate(exam) for exam in exams]


# 단일 Exam 조회 함수
def get_exam_by_id_service(db: Session, exam_id: int) -> ExamResponse:
    exam = get_exam_by_id(db, exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    return ExamResponse.model_validate(exam)


# Exam에 속한 Questions 조회 함수
def get_questions_by_exam_service(db: Session, exam_id: int, limit: Optional[int] = 10, randomize: Optional[bool] = True) -> List[QuestionResponse]:
    questions = get_questions_by_exam(db, exam_id, limit=None)
    if not questions:
        raise HTTPException(status_code=404, detail="Question not found")

    if randomize:
        questions = random.sample(questions, min(len(questions), limit))
    else:
        questions = questions[:limit]

    return [QuestionResponse.model_validate(question) for question in questions]


# Exam 수정 함수
def patch_exam_by_id_service(db: Session, exam_id: int, exam_data: ExamRequest) -> ExamResponse:
    exam = get_exam_by_id(db, exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    update_data = exam_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(exam, key, value)

    return ExamResponse.model_validate(update_exam(db, exam))


# Exam 삭제 함수
def delete_exam_by_id_service(db: Session, exam_id: int) -> ExamResponse:
    exam = get_exam_by_id(db, exam_id)
    if not exam:
        raise HTTPException(status_code=404, detail="Exam not found")

    return ExamResponse.model_validate(delete_exam(db, exam))
