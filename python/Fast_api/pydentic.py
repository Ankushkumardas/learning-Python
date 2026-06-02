# from Lib.site-packages.pydantic
from pydantic import Field
from pydantic import EmailStr,AnyUrl,field_validator,model_validator,computed_field
from typing import Optional,Annotated
from typing import Dict
from typing import List
from pydantic import BaseModel

# field_validator to add custom validation of teh fiedl data that we will send or take indise teh class we need to make 

# pydentic model or class
class A(BaseModel):
    # to make any field as optional we can do that with Optional[]
    # also can assigne defauklt values to some fiedls 
    # name:str=Field(max_length=30) -->
    name:Annotated[str,Field(max_length=30,title="Name of the patient",description="name desc",default="Ank")]
    # data valdarion for email as email has a formate so for that we use pydentic for validation 
    email:EmailStr
    url:AnyUrl
    age:int
    # field validation of check or condition liek age shoudl be always greater than 18 for teh user to apply we use Field() for that 
    weight:float=Field(gt=0,lt=200)
    height:float = 120
    married:bool = False
    # why we have not written list in place of  --> List[str]
    allergies:Optional[List[str]]
    contact_details:Dict[str,str]
    # field validatior works in 2 way s before and after and works over one field only 
    # by default teh mode i safter default
    # in teh function we will take teh class it is indsde in and teh value that we will get as prop in for the emial field
    @field_validator("email",mode="after") 
    @classmethod
    def email_validator(cls,value):
        valid=["hdfc.com","sbi.com"]
        domain=value.split("@")[-1]
        if domain not in valid:
            raise ValueError("not valid email")
        return value
        
    # model validator works over multiple fields --->
    @model_validator(mode="after")
    def validate_emerg_contact(self) -> "A":
        if self.age > 60 and "emergency" not in self.contact_details:
            raise ValueError("not possible to make pateinet account")
        return self
        
    # on the go if you need any comouted vaklues over teh vlaues that you have you can use this 
    @computed_field
    @property
    def bmi(self) -> float:
        # BMI = weight (kg) / (height (m) ^ 2)
        height_in_meters = self.height / 100
        return round(self.weight / (height_in_meters ** 2), 2)
# we use Annoted and Field to attach meta data to field ----->
def add_data(pateinet1:A):
    print(f"name is {pateinet1.name} age is {pateinet1.age} with data as married{pateinet1.married} and height is {pateinet1.height} and contact details as email : {pateinet1.contact_details["email"]} and allergies are and height is {pateinet1.height} email is {pateinet1.email} and url is {pateinet1.url} and the BMI is {pateinet1.bmi}")

data={"name":"ankush","age":60,"weight":110,"contact_details":{"city":"delhi","country":"india","email":"test@hdfc.com","phone":"234567888"},"allergies":["a","b","c"],"email":"test@hdfc.com","url":"https://www.youtube.com/watch?v=lRArylZCeOs&list=PLKnIA16_RmvZ41tjbKB2ZnwchfniNsMuQ&index=5"}

pateinet1=A(**data)

add_data(pateinet1)