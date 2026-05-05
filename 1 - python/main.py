from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from controller_alunos import ControllerAlunos

app = FastAPI()
controller = ControllerAlunos()

class AlunoBase(BaseModel):
    nome: str
    curso: str
    email_user: str

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    curso: Optional[str] = None
    email_user: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Inicio"}

@app.get("/alunos/")
async def listar_alunos():
    alunos = controller.listarAlunos()
    return [{"matricula": a.matricula, "nome": a.nome, "email": a.email, "curso": a.curso} for a in alunos]

@app.get("/alunos/{matricula}")
async def obter_aluno(matricula: str):
    aluno = controller.getAluno(matricula)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    return {"matricula": aluno.matricula, "nome": aluno.nome, "email": aluno.email, "curso": aluno.curso}

@app.post("/alunos/")
async def criar_aluno(aluno: AlunoBase):
    try:
        novo_aluno = controller.criarAluno(aluno.nome, aluno.curso, aluno.email_user)
        return {"message": "Criado com sucesso.", "aluno": {"matricula": novo_aluno.matricula, "nome": novo_aluno.nome, "email": novo_aluno.email, "curso": novo_aluno.curso}}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/alunos/{matricula}")
async def atualizar_aluno(matricula: str, aluno: AlunoBase):
    try:
        aluno_atualizado = controller.atualizarAluno(matricula, aluno.nome, aluno.curso, aluno.email_user)
        if not aluno_atualizado:
            raise HTTPException(status_code=404, detail="Aluno não encontrado.")
        return {"message": "Atualizado com sucesso.", "aluno": {"matricula": aluno_atualizado.matricula, "nome": aluno_atualizado.nome, "email": aluno_atualizado.email, "curso": aluno_atualizado.curso}}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.patch("/alunos/{matricula}")
async def patch_aluno(matricula: str, aluno: AlunoUpdate):
    try:
        aluno_atualizado = controller.atualizarAluno(matricula, aluno.nome, aluno.curso, aluno.email_user)
        if not aluno_atualizado:
            raise HTTPException(status_code=404, detail="Aluno não encontrado.")
        return {"message": "Atualizado parcialmente com sucesso.", "aluno": {"matricula": aluno_atualizado.matricula, "nome": aluno_atualizado.nome, "email": aluno_atualizado.email, "curso": aluno_atualizado.curso}}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/alunos/{matricula}")
async def deletar_aluno(matricula: str):
    aluno_deletado = controller.deletarAluno(matricula)
    if not aluno_deletado:
        raise HTTPException(status_code=404, detail="Aluno não encontrado.")
    return {"message": f"Aluno {aluno_deletado.nome} (matricula: {aluno_deletado.matricula}) deletado com sucesso."}
