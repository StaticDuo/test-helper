from pydantic import BaseModel


# 요청(Request) 스키마
class UserRequest(BaseModel):
    id: str
    password: str


# 응답(Response) 스키마
class UserResponse(BaseModel):
    user_id: int
    id: str
    password: str

    model_config = {
        "from_attributes": True  # ORM 모델과의 호환성 설정
    }
