from fastapi import FastAPI
from typing import List
from uuid import UUID, uuid4
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
  User(
    id=UUID("d638b135-5b3c-4dc5-9924-19fec7664d79"),
    first_name="Rayron",
    last_name ="Rodffer",
    gender=Gender.male,
    roles=[Role.admin, Role.user]
  ),
  User(
    id=UUID("1884c324-c6dd-45a4-90a4-e437ea8f08ca"),
    first_name="Rayfel",
    last_name ="Rodney",
    gender=Gender.male,
    roles=[Role.student]
  )
]

@app.get("/")
async def root():
  return {"message": "FastAPI with Python"}

@app.get("/api/v1/users")
async def fetch_users():
  return db