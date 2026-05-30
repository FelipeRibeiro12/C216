from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.aluno import AlunoCreate, AlunoUpdate, AlunoResponse
from app.services.aluno_service import AlunoService
from app.database import get_db

router = APIRouter()
service = AlunoService()

@router.post("/alunos/", response_model=AlunoResponse)
def criar_aluno(aluno: AlunoCreate, db: Session = Depends(get_db)):
    return service.criar(db, aluno)

@router.get("/alunos/", response_model=List[AlunoResponse])
def listar_alunos(db: Session = Depends(get_db)):
    return service.listar(db)

@router.get("/alunos/{aluno_id}", response_model=AlunoResponse)
def buscar_aluno(aluno_id: str, db: Session = Depends(get_db)):
    aluno = service.buscar_por_id(db, aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.patch("/alunos/{aluno_id}", response_model=AlunoResponse)
def atualizar_aluno(aluno_id: str, aluno: AlunoUpdate, db: Session = Depends(get_db)):
    atualizado = service.atualizar(db, aluno_id, aluno)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return atualizado

@router.delete("/alunos/{aluno_id}")
def deletar_aluno(aluno_id: str, db: Session = Depends(get_db)):
    sucesso = service.deletar(db, aluno_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"mensagem": "Aluno deletado com sucesso"}

@router.delete("/alunos/")
def deletar_todos(db: Session = Depends(get_db)):
    service.resetar(db)
    return {"mensagem": "Lista de alunos resetada com sucesso"}