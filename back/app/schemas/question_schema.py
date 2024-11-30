from pydantic import BaseModel


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

    model_config = {
        "from_attributes": True  # ORM 모델과의 호환성 설정
    }
