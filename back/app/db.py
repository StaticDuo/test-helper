from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool
from app.config import settings
import urllib.parse


# URL 인코딩 적용
encoded_password = urllib.parse.quote_plus(settings.db.DB_PASSWORD)

DATABASE_URL = f"mysql+pymysql://{settings.db.DB_USER}:{encoded_password}@{settings.db.DB_HOST}/{settings.db.DB_NAME}"

# 데이터베이스 연결 설정
engine = create_engine(
    url=DATABASE_URL,
    poolclass=QueuePool,
    pool_size=100,  # 기본 연결 수
    max_overflow=200,  # 초과 허용 연결 수
    pool_timeout=60,  # 연결 대기 시간
    pool_recycle=3600,  # 연결 재활용 시간
)

# SessionLocal 생성 (세션 팩토리)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 기본 클래스 선언
Base = declarative_base()


# 데이터베이스 세션 의존성 생성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
