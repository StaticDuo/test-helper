from pydantic import BaseModel
from typing import List, Optional


# 요청(Request) 스키마
class SubjectRequest(BaseModel):
    name: str
    description: Optional[str]


# 응답(Response) 스키마
class SubjectResponse(BaseModel):
    subject_id: int
    name: str
    description: Optional[str]

    model_config = {
        "from_attributes": True  # ORM 모델과의 호환성 설정
    }


class SubjectListResponse(BaseModel):
    message: str
    total: int
    data: List[SubjectResponse]


class SubjectDetailResponse(BaseModel):
    message: str
    data: SubjectResponse
