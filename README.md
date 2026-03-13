# Vet Clinic API

REST API developed with **FastAPI** for managing pets in a veterinary clinic.

> 🇧🇷 Projeto simples de API REST para gerenciamento de pets de uma clínica veterinária, desenvolvido com FastAPI para fins de estudo e portfólio.

---

## Features

- Create pets
- List all pets
- Get pet by ID
- Update pet
- Delete pet

---

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## Project Structure

```
api-clinica-veterinaria
│
├── app.py            # Main FastAPI application
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/api-clinica-veterinaria.git
cd api-clinica-veterinaria
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment (Windows):

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the API

Start the development server:

```bash
uvicorn app:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

---

## Example Request

Create a pet:

```json
{
  "name": "Mel",
  "species": "Dog",
  "age": 3
}
```

Response:

```json
{
  "id": 1,
  "name": "Mel",
  "species": "Dog",
  "age": 3
}
```

---

## Future Improvements

- Add database integration (PostgreSQL)
- Implement authentication
- Add automated tests
- Containerize with Docker

---

## Author

Isabella Portela