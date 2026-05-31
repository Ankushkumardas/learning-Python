# Dunder/Magic methods in python -->a sall of teh thingsin python are as objects and treated like objects


# a="csacs"
# b="bbb"
# # print(a+b)
# # the above + is internally calling a __add__ method like
# print(a.__add__(b))
# # same for length
# print(a.__len__())

class A:
    def __init__(self):
        self.value=1
    def up(self):
        self.value+=1
    def down(self):
        self.value -=1
        # __str__ get auto maticaally exceted or call even if it is not called by our side 
    def __str__(self):
        return f"the value is {self.value}"
    def __add__(self,other):
        if isinstance(other,A):
            # other=A()
            # other.value=other
            return f"the value of the added objects is {self.value+other.value}"
        else:
            raise Exception("invalid data type")
        
a1=A()
a2=A()
a1.up()
a1.up()
a2.up()
a1.down()
print(a1,a2)
print(a1+a2)


# print(a)