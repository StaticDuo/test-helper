from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db import Base


class Subject(Base):
    __tablename__ = "subjects"

    subject_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)

    exams = relationship("Exam", back_populates="subject")
