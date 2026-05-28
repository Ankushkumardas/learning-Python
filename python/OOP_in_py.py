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

a=iPhone("test",23)
print(a.buy())