# super keyword to call objects of another parent class and use them in child and super shoudl eb teh 1st statem when u call inside constrcutor class

import requests
class Phone:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def buy(self):
        print("but phone from super")

class iPhone(Phone):
    def buy(self):
        print("but iphone from super")
        super().buy()

# a=iPhone("test",23)
# print(a.buy())



# super keyword with constructor
class phone:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        print("parent")

class smartPhone(phone):
    def __init__(self,a,b,c,d):
        self.d=d
        super().__init__(a,b,c)
        print("child")

a=smartPhone(1,2,3,4)
print(a.d)

# test for api test responce 
import requests
res=requests.get('https://jsonplaceholder.typicode.com/todos?limit=2')
print(res.json())