from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class UserExam(Base):
    __tablename__ = "user_exams"

    user_exam_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    exam_id = Column(Integer, ForeignKey("exams.exam_id"), nullable=False)
    score = Column(Integer, nullable=False)
    date_taken = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="user_exams")
    exam = relationship("Exam", back_populates="user_exams")
    
    user_exam_answers = relationship("UserExamAnswer", back_populates="user_exam")
