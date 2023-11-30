import sys
sys.path.append("..")

from db.models.user import User
from db.db_setup import get_db
from sqlalchemy.orm import Session;
from db.models.schemas import UserData;

# Assuming get_db returns an SQLAlchemy session
db = get_db()

def create_user(user: UserData):
    db.add(user)
    db.commit()

def get_user(db:Session,user_id:int):
    return db.query(User).filter(User.user_id == user_id).first();

def update_user(db:Session , user_id : int , user:UserData):
    user = db.query(User).filter(User.user_id == user_id).first();
    db.refresh(user);
    db.commit();
    return "Success";

def del_user(db:Session,user_id : int,confirmation:bool):
    user = db.query(User).filter(User.user_id == user_id).first();
    if confirmation:
        db.delete(user);
        db.commit();
        print("Sucessfully Deleted");
    else:
        print("Authentication Failed");


del_user(db,2,True);