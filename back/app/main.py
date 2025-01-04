from fastapi import FastAPI, APIRouter, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.dependencies.auth import get_current_user
from app.db import engine, Base
from app.config import settings
from app.routers import subjects_router, exams_router, questions_router, answers_router, user_router

app = FastAPI()

# Swagger UI용 OpenAPI 문서 설정
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="API with JWT Authentication",
        version="1.0.0",
        description="This is an API with OAuth2PasswordBearer authentication",
        routes=app.routes,
    )
    # OAuth2PasswordBearer 설정 수정
    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",  # Bearer 방식을 사용
            "scheme": "bearer",  # JWT 인증은 Bearer 스키마를 사용
            "bearerFormat": "JWT",  # 형식 명시
        }
    }
    openapi_schema["security"] = [{"OAuth2PasswordBearer": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors.ALLOW_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# 라우터 등록

public_router = APIRouter()
public_router.include_router(user_router.public_router, tags=["user"])

protected_router = APIRouter(dependencies=[Depends(get_current_user)])
protected_router.include_router(subjects_router.router, tags=["subject"])
protected_router.include_router(exams_router.router, tags=["exam"])
protected_router.include_router(questions_router.router, tags=["question"])
protected_router.include_router(answers_router.router, tags=["answer"])
protected_router.include_router(user_router.protected_router, tags=["user"])


app.include_router(public_router)
app.include_router(protected_router)