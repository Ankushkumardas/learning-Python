from pydantic import EmailStr
from pydantic import BaseModel


class Address(BaseModel):
    city:str
    pin:int
    state:str
    
class Par(BaseModel):
    name:str
    email:EmailStr
    age:int
    address:Address
    
    
address_dict={"city":"delhi","state":"UP","pin":23456}
address1=Address(**address_dict)
pati={"name":"test","email":"test@gmail.com","age":23,"address":address1}
pateiet1=Par(**pati)

print(pateiet1)
print(pateiet1.address.city)