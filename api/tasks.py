from fastapi import APIRouter,Path;
from typing import List;
from pydantic import BaseModel;

router = APIRouter();


tasks = [];

class Task(BaseModel):
    task_id:int = len(tasks) + 1;
    task_description:str;
    task_name:str;
    is_completed:bool;
    is_deleted:bool;


@router.get("/task",response_model=List[Task])
async def get_tasks():
    return tasks;


@router.post("/tasks")
async def create_task(task:Task):
    tasks.append(task);
    return "Sucess";

@router.get("/tasks/{id}")
async def get_task_from_id(task_id:int = Path(...,description="ID of the user you want to retrieve their data" ,gt=0)):
    return tasks[task_id - 1];


@router.patch("/tasks/{id}")
async def update_task(id:int, task:Task):
    tasks[id-1] = task;
    return "Sucess";

@router.delete("/tasks/{id}")
async def del_task(task_id:int):
    del tasks[task_id - 1];
    return "Sucessfully Deleted";