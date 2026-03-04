# API Clínica Veterinária 🐾

API REST desenvolvida com **FastAPI** para gerenciamento de pets de uma clínica veterinária.

## Funcionalidades

- Cadastrar pets
- Listar pets
- Buscar pet por ID
- Remover pet

## Tecnologias

- Python
- FastAPI
- Pydantic
- Uvicorn

## Como rodar o projeto

Instalar dependências:

pip install -r requirements.txt

Rodar servidor:

python -m uvicorn app:app --reload

Acessar documentação da API:

http://127.0.0.1:8000/docs