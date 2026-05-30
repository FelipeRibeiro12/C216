from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class AlunoCreate(BaseModel):
    nome: str
    email: EmailStr
    curso: str = Field(..., pattern="^(GES|GEC)$", description="Curso deve ser GES ou GEC")

class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    curso: Optional[str] = Field(None, pattern="^(GES|GEC)$", description="Curso deve ser GES ou GEC")

class AlunoResponse(BaseModel):
    id: str
    nome: str
    email: EmailStr
    curso: str
    matricula: int

    model_config = {
        "from_attributes": True
    }
