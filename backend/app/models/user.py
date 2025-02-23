from sqlalchemy import Column, Integer, String
from db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
