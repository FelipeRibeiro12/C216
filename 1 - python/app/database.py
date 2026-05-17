import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# Lê do ambiente ou define um default para rodar local fora do docker, se necessário
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/alunos_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()