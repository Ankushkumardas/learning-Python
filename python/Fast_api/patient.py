from fastapi import status
import json
from fastapi import FastAPI,Path,HTTPException,Query

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
    # data=load_data()
    return load_data()

# path and query paarmeters -->
# the Path() function in fastapi is used to provide metadata and validation rules and documentattion hints for path para,eter in your api 
@app.get("/view/{id}")
def get_patient_by_id(id:str=Path(...,description="id od teh patient P001")):
    data=load_data()
    for key in data:
        if key==id:
            return data[key]["name"],data[key]["age"]
    # return {"error":"no data found"}
        raise HTTPException(status_code=404,detail="pateinet not found")

# query parameter--> ... dots in side teh query means that fiedl is required to put value 
@app.get('/sort')
def sort_data(sort_by:str = Query(...,description="description for sort"),order:str =Query(...,description="ascending or descrnfding order")):
    valid_fields=['height','weight']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=404,detail="invalid sort fiedl for query")
    if order not in ['asc','desc']:
        raise HTTPException(status_code=404,detail="invalid order fiedl for query")
    data=load_data()
    sort_order=True if order=="desc" else False
    # print(data.values())
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by),reverse=sort_order)
    # for i in data.values():
    #     print(i["name"])
    return sorted_data

     
# sorted() is a built-in Python function that returns a new sorted list from an iterable. By default it sorts in ascending order. The key parameter allows custom sorting logic, and reverse=True sorts in descending order.Syntax ---> sorted(iterable, key=None, reverse=False) --->sorted(products, key=lambda x: x["price"], reverse=True)
