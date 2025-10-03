from sqlmodel import create_engine, Session
from sqlmodel import SQLModel
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./leadrescue.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def init_db():
    SQLModel.metadata.create_all(engine)
    return engine

def get_session():
    return Session(engine)
