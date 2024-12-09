from .database import Base
from sqlalchemy import Column, Integer, String

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True)
    description = Column(String)