from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID
from models import User, Gender, Role, UserUpdateRequest

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

@app.post("/api/v1/users")
async def register_user(user: User):
  db.append(user)
  return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
  for user in db:
    if user.id == user_id:
      db.remove(user)
      return {"user has been removed"}
  raise HTTPException(
    status_code=404,
    detail=f"user with id: {user_id} does not exists"
  )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
  for user in db:
    if user.id == user_id:
      if user_update.first_name is not None:
        user.first_name = user_update.first_name
      if user_update.last_name is not None:
        user.last_name = user_update.last_name
      if user_update.middle_name is not None:
        user.middle_name = user_update.middle_name
      if user_update.roles is not None:
        user.roles = user_update.roles
      return {"user has been updated"}
  raise HTTPException(
    status_code=404,
    detail=f"user with id: {user_id} does not exists"
  )