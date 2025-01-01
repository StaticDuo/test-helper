from pydantic import BaseModel
from typing import List, Optional


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


# 응답 스키마 - 사용자
class AnswerUserResponse(BaseModel):
    answer_id: int
    question_id: int
    answer_text: str

    model_config = {
        "from_attributes": True  # ORM 모델과의 호환성 설정
    }


class AnswerListResponse(BaseModel):
    message: str
    total: int
    data: List[AnswerResponse]


class AnswerDetailResponse(BaseModel):
    message: str
    data: AnswerResponse
    

class AnswerUserListResponse(BaseModel):
    message: str
    total: int
    data: List[AnswerUserResponse]


class AnswerUserDetailResponse(BaseModel):
    message: str
    data: AnswerUserResponse
