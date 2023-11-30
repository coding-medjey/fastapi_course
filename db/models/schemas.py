from pydantic import BaseModel,EmailStr;
from datetime import date;


class UserData(BaseModel):
    user_id:int ;
    firstname:str;
    lastname:str;
    email : EmailStr;
    password:str;

    class Config:
        from_attributes = True;



class Task(BaseModel):
    task_id:int; 
    task_name:str; 
    task_description:str;
    created_at:date;
    ends_at:date;
    is_completed:bool;
    user_id:int; 

    class Config:
        from_attributes = True;
