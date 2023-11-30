from pydantic import BaseModel,EmailStr;
from datetime import datetime;


class UserData(BaseModel):
    firstname:str;
    lastname:str;
    email : EmailStr;
    password:str;

    class Config:
        from_attributes = True;



class TaskData(BaseModel):
    task_name:str; 
    task_description:str;
    created_at:datetime | None = datetime.now();
    ends_at:datetime | None = None;
    is_completed:bool | None = False;
    user_id:int; 

    class Config:
        from_attributes = True;
