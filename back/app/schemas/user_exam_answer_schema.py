from typing import List
from pydantic import BaseModel


# 요청(Request) 스키마
class UserExamAnswerRequest(BaseModel):
    user_exam_id: int
    question_id: int
    answer_id: int


# 응답(Response) 스키마
class UserExamAnswerResponse(BaseModel):
    user_exam_answer_id: int
    user_exam_id: int
    question_id: int
    answer_id: int

    model_config = {
        "from_attributes": True  # ORM 모델과의 호환성 설정
    }


class UserExamAnswerSubmit(BaseModel):
    question_id: int
    answer_id: int

    
class UserExamAnswerListResponse(BaseModel):
    message: str
    total: int
    data: List[UserExamAnswerResponse]
    