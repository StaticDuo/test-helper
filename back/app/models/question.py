from sqlalchemy import Column, Integer, Text, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db import Base


class Question(Base):
    __tablename__ = "questions"

    question_id = Column(Integer, primary_key=True, autoincrement=True)
    exam_id = Column(Integer, ForeignKey("exams.exam_id"), nullable=False)
    question_text = Column(Text, nullable=False)
    question_type = Column(String(10), nullable=False)  # '0': 주관식 or '1': 객관식

    exam = relationship("Exam", back_populates="questions")
    answers = relationship("Answer", back_populates="question")
