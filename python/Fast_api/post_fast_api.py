from pydantic import BaseModel
import json
from fastapi import FastAPI

app=FastAPI()

class Patient(BaseModel):
    id:str
    name:str
    city:str
    age:int
    gender:str
    height:float
    weight:float

def load_data():
    with open("patient.json","r")as f:
        data=json.load(f)
        return data

load_data()

@app.get("/")
def get_data():
    return load_data()