from pydantic import BaseModel
from typing import Optional


# 요청(Request) 스키마
class AnswerRequest(BaseModel):
    question_id: int
    answer_text: str
    is_correct: bool


# 응답(Response) 스키마
class AnswerResponse(BaseModel):
    answer_id: int
    question_id: int
    answer_text: str
    is_correct: bool

    model_config = {
        "from_attributes": True  # ORM 모델과의 호환성 설정
    }
