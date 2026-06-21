from datetime import datetime
from typing import Optional
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_db
from models.model import TodoModel

todo_routes = APIRouter(prefix="/todos", tags=["Todos"])

# Pydantic schemas
class TodoBase(BaseModel):
    name: str = Field(..., max_length=200, min_length=1, examples=["Buy milk"])
    category: Optional[str] = Field(None, max_length=200, examples=["Groceries"])
    status: bool = Field(default=False)

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=200, min_length=1)
    category: Optional[str] = Field(None, max_length=200)
    status: Optional[bool] = None

class TodoResponse(TodoBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# CRUD Routes
@todo_routes.post("", response_model=TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(todo_in: TodoCreate, db: AsyncSession = Depends(get_db)):
    todo = TodoModel(**todo_in.model_dump())
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo

@todo_routes.get("", response_model=list[TodoResponse], status_code=status.HTTP_200_OK)
async def get_all_todos(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TodoModel))
    todos = result.scalars().all()
    return todos

@todo_routes.get("/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TodoModel).where(TodoModel.id == todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@todo_routes.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(todo_id: UUID, todo_in: TodoUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TodoModel).where(TodoModel.id == todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    # Update fields that were provided
    update_data = todo_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(todo, key, value)
    
    db.add(todo)
    await db.commit()
    await db.refresh(todo)
    return todo

@todo_routes.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: UUID, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(TodoModel).where(TodoModel.id == todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    await db.delete(todo)
    await db.commit()
    return None
