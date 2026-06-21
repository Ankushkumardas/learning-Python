from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from config.db import DEFAULT_SCHEMA_NAME, Base, engine

# Import models to register them on Base.metadata before create_all is called
from models.model import TodoModel
from models.user_model import UserModel

# Import routers
from routes.todo_routes import todo_routes
from routes.user_routes import user_routes

# Lifespan context manager for startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Started")
    async with engine.begin() as conn:
        await conn.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{DEFAULT_SCHEMA_NAME}"'))
        await conn.run_sync(Base.metadata.create_all)
    yield
    
    await engine.dispose()
    print("Application stopped")

app = FastAPI(lifespan=lifespan)

# Include routers
app.include_router(todo_routes)
app.include_router(user_routes)

@app.get("/")
def read_root():
    return {"msg": "Welcome to the FastAPI Todo & User API. Visit /docs for the interactive documentation."}
