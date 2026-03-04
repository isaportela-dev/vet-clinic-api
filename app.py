from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# "Banco de dados" em memória
pets_db: dict[int, dict] = {}
next_id = 1

class PetCreate(BaseModel):
    nome: str
    especie: str
    idade: int

class Pet(PetCreate):
    id: int

@app.get("/")
def home():
    return {"mensagem": "API da Clínica Veterinária funcionando!"}

@app.get("/pets", response_model=list[Pet])
def listar_pets():
    return list(pets_db.values())

@app.post("/pets", response_model=Pet, status_code=201)
def cadastrar_pet(pet: PetCreate):
    global next_id
    novo = {"id": next_id, **pet.model_dump()}
    pets_db[next_id] = novo
    next_id += 1
    return novo

@app.get("/pets/{pet_id}", response_model=Pet)
def buscar_pet(pet_id: int):
    pet = pets_db.get(pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")
    return pet

@app.delete("/pets/{pet_id}")
def remover_pet(pet_id: int):
    pet = pets_db.pop(pet_id, None)
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")
    return {"mensagem": "Pet removido", "pet": pet}
