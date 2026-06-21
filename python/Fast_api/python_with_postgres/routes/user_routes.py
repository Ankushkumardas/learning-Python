from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_db
from models.user_model import UserModel 
from services import HashService,JwtService

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
jwt_service = JwtService()

class SignInModel(BaseModel):
    email:EmailStr
    password:str
# Simple stub GET routes (keeping what user had, but with extra instructions)
@user_routes.post("/signin",status_code=status.HTTP_200_OK)
async def signInCall(signin:SignInModel,db:AsyncSession=Depends(get_db)):
    user_db_res=await db.execute(select(UserModel).where(UserModel.email==signin.email))
    user_res=user_db_res.scalar_one_or_none()
    if not user_res:
        raise HTTPException(status_code=400,detail="User with this email does not exists!!")
    hash_pass=hash_service.verify_hash_password(signin.password,user_res.password)
    if not hash_pass:
        raise HTTPException(status_code=401,detail="Password incorrect !!")
    token=jwt_service.jwt_encode(email=signin.email)
    return {'msg':'User Signed in successfully',"jwt_token":token}


@user_routes.post("/signup",status_code=status.HTTP_201_CREATED)
async def signup(user:User,db:AsyncSession=Depends(get_db)):
    res=await db.execute(select(UserModel).where(UserModel.email==user.email))
    exisiting_user=res.scalar_one_or_none()
    if exisiting_user:
        raise HTTPException(status_code=400,detail="Email is already used")
    hashed_password = hash_service.hash_password(user.password)
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