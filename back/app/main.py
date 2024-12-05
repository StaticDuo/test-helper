from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import engine, Base
from app.config import settings
from app.routers import subjects_router, exams_router, questions_router, answers_router, user_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors.ALLOW_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

# 라우터 등록
app.include_router(subjects_router.router, tags=["subject"])
app.include_router(exams_router.router, tags=["exam"])
app.include_router(questions_router.router, tags=["question"])
app.include_router(answers_router.router, tags=["answer"])
app.include_router(user_router.router, tags=["user"])
