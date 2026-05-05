# Gerenciamento de Alunos — API Rest com FastAPI e Docker

## Tech Stack

[![My Skills](https://skillicons.dev/icons?i=python,fastapi,docker)](https://skillicons.dev)

## Estrutura do diretório

- `app/` — Diretório principal da aplicação
  - `main.py` — Ponto de entrada (entrypoint) da API
  - `routes/` — Definição das rotas (endpoints) do CRUD
  - `services/` — Camada de serviço contendo as regras de negócio
  - `schemas/` — Modelos de validação de dados utilizando Pydantic
  - `middlewares/` — Interceptadores e modificadores de requisições globais
- `tests/` — Testes automatizados da aplicação
- `Dockerfile` — Instruções para a criação da imagem da aplicação
- `requirements.txt` — Dependências do projeto

## Iniciando

1. Certifique-se de ter o [Docker](https://www.docker.com/) instalado em sua máquina.

2. Acesse a raiz do repositório no seu comando/terminal:

```bash
cd "Y:\Inatel\P10\C216"
```

3. Inicie a API executando o Docker Compose:

```bash
docker-compose up --build -d api
```

A aplicação estará rodando na porta `8000`.

## Testes Automatizados

Para executar a validação dos testes com Pytest, insira o seguinte comando:

```bash
docker-compose run tests
```

## Documentação útil

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Docker Docs](https://docs.docker.com/)
