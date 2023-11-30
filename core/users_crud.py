import sys
sys.path.append("..")

from db.models.user import User
from sqlalchemy.orm import Session;
from db.models.schemas import UserData;
from sqlalchemy.exc import SQLAlchemyError;



def create_user(db:Session ,user: UserData):
    try:
        user_data = User(**user.dict());
        db.add(user_data)
        db.commit()
        return True;
    except SQLAlchemyError as e:  
        print(e); 
        return False;
    

def get_user(db:Session,user_id:int):
    user = db.query(User).filter(User.user_id == user_id).first();
    if user:
        return user;
    else:
        print("No user found");
        return False;

def update_user(db: Session, user_id: int, user: UserData):
    user_data = db.query(User).filter(User.user_id == user_id).first()

    if user_data:
        for field, value in user.dict().items():
            setattr(user_data, field, value)

        db.commit()
        db.refresh(user_data)
        return True
    else:
        print("User not found")
        return False


def del_user(db:Session,user_id : int,confirmation:bool):
    user = db.query(User).filter(User.user_id == user_id).first();
    if user and confirmation:
        db.delete(user);
        db.commit();
        print("Sucessfully Deleted");
        return True;
    else:
        print("Authentication Failed");
        return False;


