from sqlalchemy import true
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL= "postgresql+asyncpg://admin:password@localhost:5432/todo_db"
DEFAULT_SCHEMA_NAME= "Todo_s"

metadata=MetaData(schema=DEFAULT_SCHEMA_NAME)

class Base(DeclarativeBase):
    pass

engine=create_async_engine(
    DATABASE_URL,
    echo=True
)

Async_Session_Local=async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with Async_Session_Local() as session:
        yield session