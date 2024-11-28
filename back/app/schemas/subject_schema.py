from pydantic import BaseModel
from typing import Optional


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
