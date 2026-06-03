from typing import Optional
from typing import Literal
from pydantic import Field,computed_field
from typing import Annotated
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import json
from fastapi import FastAPI,HTTPException

app=FastAPI()

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="id is a valid is always required field")]
    name:str
    city:str
    age:Annotated[int,Field(...,gt=0, lt=100,description="age field")]
    # literal works as options or enum
    gender:Annotated[Literal["male","female","other"],Field(...,description="gender of teh person")]
    height: Annotated[float, Field(..., gt=0, description="Height in meters")]
    weight: Annotated[float, Field(..., gt=0, description="Weight in kilograms")]


    @computed_field
    @property
    def bmi(self) -> float:
        # BMI = weight (kg) / (height (m) ^ 2)
        # If height is in centimeters (e.g. 170), convert it to meters (1.7)
        h = self.height / 100 if self.height > 3 else self.height
        res = round(self.weight / (h**2), 2)
        return res
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Over weight"
        else:
            return "Obese"
            
class PatientUpdate(BaseModel):  
    id: Annotated[Optional[str], Field(default=None)] = None
    name: Optional[str] = None
    city: Optional[str] = None
    age: Annotated[Optional[int], Field(gt=0, lt=100, default=None)] = None
    gender: Annotated[Optional[Literal["male", "female", "other"]], Field(default=None)] = None
    height: Annotated[Optional[float], Field(gt=0, default=None)] = None
    weight: Annotated[Optional[float], Field(gt=0, default=None)] = None

def load_data():
    with open("patient.json","r")as f:
        data=json.load(f)
        return data

# save data
def save_data(data):
    with open("patient.json","w") as f:
        json.dump(data, f, indent=4)

@app.get("/")
def get_data():
    return load_data()

@app.post('/create')
def create_patient(patient:Patient):
    # load all exisitng data and check if data with same id already exisits or not i fnot add teh new json data 
    data=load_data()
    if patient.id in data:
        raise HTTPException(status_code=400,detail="patient with this ID aleady exists")
    # add the new patient data
    # model_dump Convert Pydantic object → Python dictionary
    data[patient.id]=patient.model_dump(exclude={'id'})
    # "Use the patient's ID as the dictionary key, store all the other patient details as the value, save it to a JSON file, and return the updated data."
    # with open("patient.json","w")as f:
    #     json.dump(data,f,indent=4)
    save_data(data)
    return JSONResponse(status_code=201,content={"message":"Pateinet data added sucecssfully"})

# @app.put("/patient/{id}")
# def update_patient(id:str,patient:PatientUpdate):
#     data=load_data()
#     if id not in data:
#         raise HTTPException(status_code=400,detail="Patient with this id is not available")
#     data[id]=patient.model_dump(exclude={"id"})
#     save_data(data)
#     return JSONResponse(status_code=200,content={"message":f"Data updated for user id : {id} with data {data[id]}"})

@app.patch("/patient/{id}")
def update_patch_data(id:str,patient:PatientUpdate):
    data=load_data()
    if id not in data:
        raise HTTPException(status_code=400,detail=f"data with this is not found {id}")
    
    # 1. Get the existing patient dictionary (without "id" as keys are IDs in JSON)
    existing_patient = data[id]
    
    # 2. Add the id to the dict temporarily for Patient validation and computed fields
    existing_patient["id"] = id
    
    # 3. Get the fields that the user sent to update
    updated_fields = patient.model_dump(exclude_unset=True)
    
    # 4. Merge updated fields into existing_patient
    for key, value in updated_fields.items():
        if key == "id":
            continue
        existing_patient[key] = value
        
    # 5. Instantiate Patient to validate merged data and recalculate bmi/verdict
    patient_pydantic = Patient(**existing_patient)
    
    # 6. Serialize updated patient data back without the "id" key
    updated_patient_dict = patient_pydantic.model_dump(exclude={"id"})
    
    # 7. Save the entire dataset
    data[id] = updated_patient_dict
    save_data(data)
    
    return JSONResponse(status_code=200,content={"message": f"Data updated partially with patch api call data: {data[id]}"})

@app.delete("/patient/{id}")
def del_data(id:str):
    data=load_data()
    if id not in data:
        raise HTTPException(status_code=400,detail=f"no data found to dleet on  thi sid  {id}")
    del(data[id])
    save_data(data)
    return JSONResponse(status_code=201,content={"message":f"patient fdata delete on id {id} "})