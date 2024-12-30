from typing import List
from pydantic import BaseModel

from app.schemas.answer_schema import AnswerUserResponse


# 요청(Request) 스키마
class QuestionRequest(BaseModel):
    exam_id: int
    question_number: int
    question_text: str
    question_type: str


# 응답(Response) 스키마
class QuestionResponse(BaseModel):
    question_id: int
    exam_id: int
    question_number: int
    question_text: str
    question_type: str
    answers: List[AnswerUserResponse]

    model_config = {
        "from_attributes": True  # ORM 모델과의 호환성 설정
    }


class QuestionListResponse(BaseModel):
    message: str
    total: int
    data: List[QuestionResponse]


class QuestionDetailResponse(BaseModel):
    message: str
    data: QuestionResponse