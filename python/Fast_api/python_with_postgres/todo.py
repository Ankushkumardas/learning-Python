from contextlib import asynccontextmanager
from fastapi import FastAPI
from config.db import DEFAULT_SCHEMA_NAME, Base, engine
from sqlalchemy import text

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application Started")
    async with engine.begin() as conn:
        await conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {DEFAULT_SCHEMA_NAME}"))
        await conn.run_sync(Base.metadata.create_all)
    yield
    
    await engine.dispose()
    print("Application stopped")

# fast api call
app=FastAPI(lifespan=lifespan)
