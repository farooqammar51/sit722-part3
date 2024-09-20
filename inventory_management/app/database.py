from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://s222611966_sit722_part3_user:kTdz67XTqrx6wwpBwa1XpYrg95iAwr79@dpg-crmr4s88fa8c73ani740-a.oregon-postgres.render.com/s222611966_sit722_part3" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
