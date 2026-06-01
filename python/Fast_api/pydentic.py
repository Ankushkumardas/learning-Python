from pydantic import BaseModel

class A(BaseModel):
    name:str
    age:int

def add_data(pateinet1:A):
    print(f"name is {pateinet1.name} age is {pateinet1.age}")

data={"name":"ankush","age":22}
pateinet1=A(**data)

add_data(pateinet1)