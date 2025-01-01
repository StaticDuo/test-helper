from typing import List
from pydantic import BaseModel


# 요청(Request) 스키마
class UserRequest(BaseModel):
    email: str
    password: str


# 응답(Response) 스키마
class UserResponse(BaseModel):
    user_id: int
    email: str
    password: str

    model_config = {
        "from_attributes": True  # ORM 모델과의 호환성 설정
    }


class UserListResponse(BaseModel):
    message: str
    total: int
    data: List[UserResponse]


class UserJWTResponse(BaseModel):
    token_type: str
    access_token: str
    refresh_token: str


class UserDetailResponse(BaseModel):
    message: str
    data: UserResponse


class UserJWTDetailResponse(BaseModel):
    message: str
    data: UserJWTResponse
