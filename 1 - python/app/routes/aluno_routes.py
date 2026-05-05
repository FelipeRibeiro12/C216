from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.aluno import AlunoCreate, AlunoUpdate, AlunoResponse
from app.services.aluno_service import AlunoService

router = APIRouter()
service = AlunoService()

@router.post("/alunos/", response_model=AlunoResponse)
def criar_aluno(aluno: AlunoCreate):
    return service.criar(aluno)

@router.get("/alunos/", response_model=List[AlunoResponse])
def listar_alunos():
    return service.listar()

@router.get("/alunos/{aluno_id}", response_model=AlunoResponse)
def buscar_aluno(aluno_id: str):
    aluno = service.buscar_por_id(aluno_id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.patch("/alunos/{aluno_id}", response_model=AlunoResponse)
def atualizar_aluno(aluno_id: str, aluno: AlunoUpdate):
    atualizado = service.atualizar(aluno_id, aluno)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return atualizado

@router.delete("/alunos/{aluno_id}")
def deletar_aluno(aluno_id: str):
    sucesso = service.deletar(aluno_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"mensagem": "Aluno deletado com sucesso"}

@router.delete("/alunos/")
def deletar_todos():
    service.resetar()
    return {"mensagem": "Lista de alunos resetada com sucesso"}