from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_reset_inicial():
    client.delete("/api/v1/alunos/")

def test_criar_alunos_gec():
    for i in range(1, 4):
        response = client.post("/api/v1/alunos/", json={
            "nome": f"Aluno GEC {i}",
            "email": f"gec{i}@inatel.br",
            "curso": "GEC"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == f"GEC{i}"
        assert data["matricula"] == i
        assert data["curso"] == "GEC"

def test_criar_alunos_ges():
    for i in range(1, 4):
        response = client.post("/api/v1/alunos/", json={
            "nome": f"Aluno GES {i}",
            "email": f"ges{i}@inatel.br",
            "curso": "GES"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == f"GES{i}"
        assert data["matricula"] == i
        assert data["curso"] == "GES"

def test_listar_alunos():
    response = client.get("/api/v1/alunos/")
    assert response.status_code == 200
    assert len(response.json()) == 6

def test_buscar_aluno_por_id():
    response = client.get("/api/v1/alunos/GEC1")
    assert response.status_code == 200
    assert response.json()["nome"] == "Aluno GEC 1"

def test_atualizar_aluno():
    response = client.patch("/api/v1/alunos/GES1", json={
        "nome": "GES 1 Atualizado",
        "email": "novo@ges.inatel.br"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["nome"] == "GES 1 Atualizado"
    assert data["email"] == "novo@ges.inatel.br"

def test_deletar_aluno():
    response = client.delete("/api/v1/alunos/GEC2")
    assert response.status_code == 200
    assert response.json()["mensagem"] == "Aluno deletado com sucesso"

    # Confirma que foi deletado
    response_check = client.get("/api/v1/alunos/GEC2")
    assert response_check.status_code == 404

def test_matricula_nao_reutilizada():
    # Cria mais um aluno GEC após exclusão do 2. Deve ser GEC4
    response = client.post("/api/v1/alunos/", json={
        "nome": "Novo Aluno GEC",
        "email": "gec_novo@inatel.br",
        "curso": "GEC"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "GEC4"
    assert data["matricula"] == 4