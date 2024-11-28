from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import QueuePool
from dotenv import load_dotenv
import os
import urllib.parse

# 환경 변수 로드
load_dotenv()

# 데이터베이스 접근정보
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

# URL 인코딩 적용
encoded_password = urllib.parse.quote_plus(db_password)

DATABASE_URL = f"mysql+pymysql://{db_user}:{encoded_password}@{db_host}/{db_name}"

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
