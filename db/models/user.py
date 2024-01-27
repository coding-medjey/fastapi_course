from sqlalchemy import Column , Integer ,String;
from sqlalchemy.orm import relationship;
from ..db_setup import Base;


class User(Base):
    __tablename__ = "users";

    user_id = Column(Integer , primary_key=True,index = True,autoincrement = True,nullable=False);
    firstname = Column(String(255),nullable = False);
    lastname = Column(String(255),nullable=False,index = True);
    email = Column(String(255),nullable=False,unique=True,index = True);
    password = Column(String(18),nullable = False,index=True);
    tasks = relationship('Task', back_populates='user');


