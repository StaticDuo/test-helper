from pydantic import BaseModel
from typing import List, Optional


# 요청(Request) 스키마
class ExamRequest(BaseModel):
    subject_id: int
    name: str


# 응답(Response) 스키마
class ExamResponse(BaseModel):
    exam_id: int
    subject_id: int
    name: str

    model_config = {
        "from_attributes": True  # ORM 모델과의 호환성 설정
    }


class ExamListResponse(BaseModel):
    message: str
    total: int
    data: List[ExamResponse]


class ExamDetailResponse(BaseModel):
    message: str
    data: ExamResponse
