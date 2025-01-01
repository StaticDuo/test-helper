from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from app.models.exam import Exam
from app.models.user_exam import UserExam
from app.models.user import User
from typing import List, Optional


# User 생성
def create_user(db: Session, user: User) -> User:
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError:
        db.rollback()
        raise


# User 조회
def get_users(db: Session, email: Optional[str] = None):
    query = db.query(User)

    if email:
        query = query.filter(User.email.ilike(f"%{email}%"))

    return query.all()


# 단일 User 조회
def get_user_by_id(db: Session, user_id: str) -> User:
    return db.query(User).filter(User.user_id == user_id).first()


# 단일 User 조회 by email
def get_user_by_email(db: Session, email: str) -> User:
    return db.query(User).filter(User.email == email).first()


# 응시한 Exam 조회 by User id
def get_exam_by_user(db: Session, user_id: int, limit: Optional[int] = 10) -> List[Exam]:
    sort_column = getattr(UserExam, "date_taken", None)
    sort_order = sort_column.desc()

    query = (
        db.query(Exam)
        .join(UserExam, UserExam.exam_id == Exam.exam_id)
        .options(joinedload(Exam.user_exams), joinedload(Exam.subject))
        .filter(UserExam.user_id == user_id)
        .order_by(sort_order)
    )
    
    if limit:
        query = query.limit(limit)

    print(query)
    return query.all()
