from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_db
from models.user_model import UserModel 
from services import HashService

user_routes = APIRouter(prefix="/users", tags=["Users"])

# Pydantic schemas to avoid naming conflicts with DBUserModel
class User(BaseModel):
    name: str = Field(..., max_length=200, min_length=1, examples=["John Doe"])
    email: EmailStr = Field(..., examples=["john.doe@example.com"])
    password:str=Field(...,examples=["sfsafsafas"])

    class Config:
        from_attributes = True

class UserCreateResponce(BaseModel):
    # id:UUID
    name:str
    email:EmailStr
    msg:str
    
    class Config:
        from_attributes=True
        
# Service configuration
hash_service = HashService()

# Simple stub GET routes (keeping what user had, but with extra instructions)
@user_routes.get("/signin")
def signInCall():
    return {"msg": "Get api call for users signin (Use POST /users/signin for active authentication)"}

@user_routes.post("/signup",status_code=status.HTTP_201_CREATED)
async def signup(user:User,db:AsyncSession=Depends(get_db)):
    res=await db.execute(select(UserModel).where(UserModel.email==user.email))
    exisiting_user=res.scalar_one_or_none()
    if(exisiting_user):
        raise HTTPException(status_code=400,detail="Email is already used")
    hashed_password = hash_service.hashpassword(user.password)
    db_user = UserModel(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return UserCreateResponce(
        name=user.name,email=user.email,msg="user create successfully "
    )