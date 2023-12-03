from sqlalchemy import Column, Integer, String

from database import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    hashed_password = Column(String(100))
