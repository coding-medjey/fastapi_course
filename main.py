from typing import List;
from fastapi import FastAPI , Path;
from pydantic import BaseModel;

users = [];

class User(BaseModel):
    user_id:int = len(users) + 1;
    firstname:str;
    lastname:str;
    email:str;
    password:str;

app = FastAPI();

@app.get("/users",response_model=List[User])
async def get_users():
    return users;


@app.post("/users")
async def create_user(user:User):
    users.append(user);
    return "Sucess";

@app.get("/users/{id}")
async def get_user_from_id(id:int = Path(...,description="ID of the user you want to retrieve their data" ,gt=0)):
    return users[id - 1];