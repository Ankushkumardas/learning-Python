# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# class Tea(BaseModel):
#     id: str
#     name: str
#     origin: str

# teas: List[Tea] = []

# @app.get("/")
# def root():
#     return {"message": "This is the get request with decorator"}

# @app.get("/teas")
# def get_teas():
#     return teas

# @app.post("/teas")
# def add_tea(tea: Tea):
#     teas.append(tea)
#     return teas

# @app.put("/teas/{id}")
# def update_tea(id: str, data: Tea):
#     for i, t in enumerate(teas):
#         if t.id == id:
#             teas[i] = data
#             return data
#     return {"error": "Tea not found"}

# @app.delete("/teas/{id}")
# def del_tea(id: str):
#     for i, t in enumerate(teas):
#         if t.id == id:
#             removed_tea = teas.pop(i)
#             return removed_tea
#     return {"error": "Tea not found"}


