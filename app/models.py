from sqlalchemy import Column, Integer, String, Boolean, Date
from .database import Base

#Define Model
class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    due_date = Column(Date, nullable=True)

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    priority = Column(Integer, default=1)
    #給另外一個人改
class User(Base):
    __tablename__="Users"
    id = Column(Integer, primary_key=True, index=True)
    