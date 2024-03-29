from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os


"""
Postgres db connection
"""
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" # for Sqlite
SQLALCHEMY_DATABASE_URL = os.environ['DatabaseURL'] #for docker-compose and kubernetes
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/db" #normal run 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL  # connect_args={"check_same_thread": False} #second argument needed only for sqlite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
