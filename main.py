from fastapi import FastAPI;
from api import users,tasks;
from db.db_setup import engine;



app = FastAPI();



app.include_router(users.router);
app.include_router(tasks.router);

