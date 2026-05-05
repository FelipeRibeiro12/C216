from typing import List, Optional
from app.schemas.aluno import AlunoCreate, AlunoUpdate, AlunoResponse

class AlunoService:
    def __init__(self):
        self._alunos = []
        self._counters = {
            "GES": 0,
            "GEC": 0
        }

    def listar(self) -> List[AlunoResponse]:
        return self._alunos

    def buscar_por_id(self, aluno_id: str) -> Optional[AlunoResponse]:
        for aluno in self._alunos:
            if aluno.id == aluno_id.upper():
                return aluno
        return None

    def criar(self, aluno_data: AlunoCreate) -> AlunoResponse:
        curso = aluno_data.curso.upper()
        self._counters[curso] += 1
        matricula = self._counters[curso]
        aluno_id = f"{curso}{matricula}"
        
        novo_aluno = AlunoResponse(
            id=aluno_id,
            matricula=matricula,
            nome=aluno_data.nome,
            email=aluno_data.email,
            curso=curso
        )
        self._alunos.append(novo_aluno)
        return novo_aluno

    def atualizar(self, aluno_id: str, aluno_data: AlunoUpdate) -> Optional[AlunoResponse]:
        aluno = self.buscar_por_id(aluno_id)
        if aluno:
            if aluno_data.nome is not None:
                aluno.nome = aluno_data.nome
            if aluno_data.email is not None:
                aluno.email = aluno_data.email
            if aluno_data.curso is not None:
                aluno.curso = aluno_data.curso.upper()
            return aluno
        return None

    def deletar(self, aluno_id: str) -> bool:
        aluno = self.buscar_por_id(aluno_id)
        if aluno:
            self._alunos.remove(aluno)
            return True
        return False

    def resetar(self) -> bool:
        self._alunos.clear()
        return True