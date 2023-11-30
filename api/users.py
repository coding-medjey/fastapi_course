from fastapi import APIRouter , Path;
from typing import List;
from pydantic import BaseModel;

router = APIRouter();


users = [];

class User(BaseModel):
    user_id:int = len(users) + 1;
    firstname:str;
    lastname:str;
    email:str;
    password:str;


@router.get("/users",response_model=List[User])
async def get_users():
    return users;


@router.post("/users")
async def create_user(user:User):
    users.append(user);
    return "Sucess";

@router.get("/users/{id}")
async def get_user_from_id(id:int = Path(...,description="ID of the user you want to retrieve their data" ,gt=0)):
    return users[id - 1];


@router.patch("/users/{id}")
async def update_user(user:User):
    return "Sucess";

@router.delete("/users/{id}")
async def del_user(id:int):
    return "Sucessfully Deleted";