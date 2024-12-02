from sqlalchemy import Column, Integer, String
from app.db import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
