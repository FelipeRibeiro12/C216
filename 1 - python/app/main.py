from fastapi import FastAPI

from app.routes.aluno_routes import router as aluno_router
from app.middlewares.logging import log_requests
from app.middlewares.custom_header import add_custom_header
from app.database import Base, engine
from app.models.aluno import AlunoModel

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gerenciador de Alunos API PostgreSQL",
    description="API para testes de CRUD de Alunos com FastAPI e Docker",
    version="1.0.0"
)

app.middleware("http")(log_requests)
app.middleware("http")(add_custom_header)

app.include_router(aluno_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"mensagem": "API Ativa"}