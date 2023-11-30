import sys;
sys.path.append("..");

from db.models.task import Task;
from db.models.schemas import TaskData;
from sqlalchemy.orm import Session;
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime;
from db.db_setup import get_db;

db = get_db();

def create_task(db:Session ,task:TaskData):
    try:
        task_data = Task(**task.model_dump());
        db.add(task_data);
        db.commit();
        return True;
    except SQLAlchemyError as e:
        print(e);
        return False;


def get_tasks(db:Session,id:int):
    tasks = db.query(Task).filter(Task.user_id == id);
    task_list = [];
    for task in tasks:
        task_list.append(task);
    if len(task_list) != 0:
        return task_list;
    else:
        return None;

def update_tasks(db:Session,task_id : int,task:TaskData):
    existing_task = db.query(Task).filter(Task.task_id == task_id).first();
    if existing_task is None:
        return False;
    for field , value in task.model_dump().items():
        setattr(existing_task,field,value);
    db.commit();
    db.refresh(existing_task);
    return True;


def del_task(db:Session,task_id:int,confirmation:bool):
    task = db.query(Task).filter(Task.task_id == task_id).first();
    if task and confirmation:
        db.delete(task);
        db.commit();
        print("Sucessfully Deleted");
        return True;
    else:
        print("Something Happened");
        return False;



