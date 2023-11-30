import sys
sys.path.append("..")

from fastapi import APIRouter , Path
from typing import List;
from db.models.schemas import UserData;
from db.db_setup import get_db;
from core.users_crud import create_user , get_user , update_user , del_user;

router = APIRouter();

db = get_db();



@router.get("/users/{id}")
async def get_user_from_id(id:int = Path(...,description="ID of the user you want to retrieve their data" ,gt=0)):
    return {"user":get_user(db,id)}

@router.post("/signin")
async def create_user_(user:UserData):
    return create_user(db,user);

@router.put("/update_user/{id}")
async def updating_user(user:UserData , id:int):
    print(id , user);
    return update_user(db,id,user);

@router.delete("/delete_user")
async def delete_user(id:int,confirmation : bool):
    return del_user(db,id,confirmation);