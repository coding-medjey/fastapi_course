from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_DATABASE_URL = "mysql+pymysql://root:Bhirahatees_123@localhost:3306/task_management_app";

engine = create_engine(_DATABASE_URL , future=True);

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine,future = True)

Base = declarative_base()


#DB Utils

def get_db():
    db = SessionLocal();
    try:
        return db;
    finally:
        db.close();