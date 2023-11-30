import sys
sys.path.append("..")

from fastapi import APIRouter,Path;
from db.models.schemas import TaskData;
from db.db_setup import get_db;
from core.task_crud import create_task , get_tasks , update_tasks , del_task;


router = APIRouter();

db = get_db();

@router.get("/tasks/{task_id}")
async def get_task(task_id:int):
    tasks = get_tasks(db,task_id)
    return {"tasks" : tasks};

@router.post("/create_task")
async def create_tasks(task:TaskData):
    return create_task(db,task);

@router.put("/update_task/{id}")
async def update_task(id:int,task:TaskData):
    return update_tasks(db,id,task);

@router.delete("/delete_task")
async def delete_task(id:int,confirmation:bool):
    return del_task(db,id,confirmation);