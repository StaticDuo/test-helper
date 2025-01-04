from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base


class UserExamAnswer(Base):
    __tablename__ = "user_exam_answers"

    user_exam_answer_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_exam_id = Column(Integer, ForeignKey("user_exams.user_exam_id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.question_id"), nullable=False)
    answer_id = Column(Integer, ForeignKey("answers.answer_id"), nullable=False)
    
    user_exam = relationship("UserExam", back_populates="user_exam_answers")
    
    questions = relationship("Question", back_populates="user_exam_answer")
    answers = relationship("Answer", back_populates="user_exam_answer")
    