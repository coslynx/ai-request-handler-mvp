from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError
import os
from datetime import datetime

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=100), unique=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class RequestLog(Base):
    __tablename__ = 'request_logs'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    prompt = Column(Text, nullable=False)
    response = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_user(username: str):
    db = next(get_db())
    user = User(username=username)
    db.add(user)
    try:
        db.commit()
        db.refresh(user)
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Database error: {str(e)}")
    return user

def get_user(user_id: int):
    db = next(get_db())
    return db.query(User).filter(User.id == user_id).first()

def create_request_log(user_id: int, prompt: str, response: str):
    db = next(get_db())
    request_log = RequestLog(user_id=user_id, prompt=prompt, response=response)
    db.add(request_log)
    try:
        db.commit()
        db.refresh(request_log)
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Database error: {str(e)}")
    return request_log

def get_request_logs(user_id: int):
    db = next(get_db())
    return db.query(RequestLog).filter(RequestLog.user_id == user_id).all()