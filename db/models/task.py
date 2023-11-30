from sqlalchemy import Column,String,Integer , Boolean,Text,Date,ForeignKey;
from sqlalchemy.orm import relationship
from ..db_setup import Base;



class Task(Base):
    __tablename__ = "tasks";

    task_id = Column(Integer,autoincrement=True,primary_key=True,nullable=False,index=True);
    task_name = Column(String(255),nullable=False,index=True);
    task_description = Column(Text(400),nullable=False,index=True);
    created_at = Column(Date , nullable = False,index=True);
    ends_at = Column(Date,nullable=True,index=True);
    is_completed = Column(Boolean , nullable=False,index=True);
    user_id = Column(Integer,ForeignKey("users.user_id"),nullable=False);
