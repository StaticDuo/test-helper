from pydantic import BaseModel
from datetime import datetime


# 응답(Response) 스키마
class UserExamResponse(BaseModel):
    user_exam_id: int
    exam_id: int
    score: int
    date_taken: datetime

    model_config = {
        "from_attributes": True  # ORM 모델과의 호환성 설정
    }
    