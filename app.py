from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Vet Clinic API")


# In-memory database
pets_db: dict[int, dict] = {}
next_id = 1


class PetCreate(BaseModel):
    name: str = Field(..., min_length=1, example="Mel")
    species: str = Field(..., min_length=1, example="Dog")
    age: int = Field(..., ge=0, example=3)


class Pet(BaseModel):
    id: int
    name: str
    species: str
    age: int


@app.get("/")
def home():
    return {"message": "Vet Clinic API is running!"}


@app.get("/pets", response_model=list[Pet])
def list_pets():
    return list(pets_db.values())


@app.post("/pets", response_model=Pet, status_code=201)
def create_pet(pet: PetCreate):
    global next_id

    new_pet = {
        "id": next_id,
        "name": pet.name,
        "species": pet.species,
        "age": pet.age,
    }

    pets_db[next_id] = new_pet
    next_id += 1

    return new_pet


@app.get("/pets/{pet_id}", response_model=Pet)
def get_pet(pet_id: int):
    pet = pets_db.get(pet_id)

    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    return pet


@app.put("/pets/{pet_id}", response_model=Pet)
def update_pet(pet_id: int, updated_pet: PetCreate):
    if pet_id not in pets_db:
        raise HTTPException(status_code=404, detail="Pet not found")

    pet = {
        "id": pet_id,
        "name": updated_pet.name,
        "species": updated_pet.species,
        "age": updated_pet.age,
    }

    pets_db[pet_id] = pet
    return pet


@app.delete("/pets/{pet_id}")
def delete_pet(pet_id: int):
    if pet_id not in pets_db:
        raise HTTPException(status_code=404, detail="Pet not found")

    deleted_pet = pets_db.pop(pet_id)
    return {
        "message": "Pet deleted successfully",
        "pet": deleted_pet
    }