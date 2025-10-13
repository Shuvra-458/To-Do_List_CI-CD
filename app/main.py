# app/main.py
from fastapi import FastAPI
from .database import engine, Base
from .routes import tasks

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do List API")

# Include routes
app.include_router(tasks.router)
