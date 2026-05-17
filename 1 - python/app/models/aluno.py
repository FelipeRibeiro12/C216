from sqlalchemy import Column, Integer, String, Sequence
from app.database import Base

class AlunoModel(Base):
    __tablename__ = "alunos"

    id = Column(String, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    curso = Column(String, nullable=False)
    matricula = Column(Integer, nullable=False)