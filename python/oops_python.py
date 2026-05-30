# OOPS

class a:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
        # self.details
        # print(name)
    def details(self):
        print(f'{self.name} is the name of the student with age {self.__age}')

a1=a("ank",11)
a1.details()
# print(a1.__dict__)


# features of OOPS-->
# abstraction -- hidding unnecasry details from class or methods 
# encapsulation -- resstrict access to certain attributes from other users 
# inheritance
# polymorphism

