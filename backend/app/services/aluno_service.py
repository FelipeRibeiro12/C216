from sqlalchemy.orm import Session
from app.models.aluno import AlunoModel
from app.schemas.aluno import AlunoCreate, AlunoUpdate, AlunoResponse
from typing import List, Optional

class AlunoService:
    def listar(self, db: Session) -> List[AlunoResponse]:
        alunos_orm = db.query(AlunoModel).all()
        return [AlunoResponse.model_validate(a, from_attributes=True) for a in alunos_orm]

    def buscar_por_id(self, db: Session, aluno_id: str) -> Optional[AlunoResponse]:
        aluno = db.query(AlunoModel).filter(AlunoModel.id == aluno_id.upper()).first()
        if aluno:
            return AlunoResponse.model_validate(aluno, from_attributes=True)
        return None

    def _obter_proxima_matricula(self, db: Session, curso: str) -> int:
        from sqlalchemy import func
        resultado = db.query(func.max(AlunoModel.matricula)).filter(AlunoModel.curso == curso).scalar()
        if resultado is None:
            return 1
        return resultado + 1

    def criar(self, db: Session, aluno_data: AlunoCreate) -> AlunoResponse:
        curso = aluno_data.curso.upper()
        matricula = self._obter_proxima_matricula(db, curso)
        aluno_id = f"{curso}{matricula}"
        
        novo_aluno = AlunoModel(
            id=aluno_id,
            matricula=matricula,
            nome=aluno_data.nome,
            email=aluno_data.email,
            curso=curso
        )
        db.add(novo_aluno)
        db.commit()
        db.refresh(novo_aluno)
        
        return AlunoResponse.model_validate(novo_aluno, from_attributes=True)

    def atualizar(self, db: Session, aluno_id: str, aluno_data: AlunoUpdate) -> Optional[AlunoResponse]:
        aluno = db.query(AlunoModel).filter(AlunoModel.id == aluno_id.upper()).first()
        if not aluno:
            return None

        if aluno_data.nome is not None:
            aluno.nome = aluno_data.nome
        if aluno_data.email is not None:
            aluno.email = aluno_data.email
        if aluno_data.curso is not None:
             aluno.curso = aluno_data.curso.upper()

        db.commit()
        db.refresh(aluno)
        return AlunoResponse.model_validate(aluno, from_attributes=True)

    def deletar(self, db: Session, aluno_id: str) -> bool:
        aluno = db.query(AlunoModel).filter(AlunoModel.id == aluno_id.upper()).first()
        if aluno:
            db.delete(aluno)
            db.commit()
            return True
        return False

    def resetar(self, db: Session) -> bool:
        db.query(AlunoModel).delete()
        db.commit()
        return True