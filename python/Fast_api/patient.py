from fastapi import status
import json
from fastapi import FastAPI,Path,HTTPException

app=FastAPI()

def load_data():
    with open('patient.json','r') as f:
        data=json.load(f)
        return data

@app.get("/")
def get_data():
    return {"data":"this is the test get url responce"}

@app.get("/view")
def get_all_data():
    return load_data()

# path and query paarmeters -->
# the Path() function in fastapi is used to provide metadata and validation rules and documentattion hints for path para,eter in your api 
@app.get("/view/{id}")
def get_patient_by_id(id:str=Path(...,description="id od teh patient P001")):
    data=load_data()
    for key in data:
        if key==id:
            return data[key]
    # return {"error":"no data found"}
        raise HTTPException(status_code=404,detail="pateinet not found")
