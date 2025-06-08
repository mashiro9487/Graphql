from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    email = Column(String, primary_key=True, nullable=False)
    password = Column(String)
