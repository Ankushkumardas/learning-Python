# aliasing 

# a=5
# b=a
# print(id(a))
# print(id(b))

#both will have teh same memory address in the RAM and memory location

# garbaze collection


# in aliasing in pyhtin while assigneing value to a  variable if we again  reassign it we get teh same id of teh initial variable 

# a="hey"
# a=a+"hello"+"world"
# print(a)

# cloning in python

l1=[1,2,3,4,5]
l2=l1
l3=l1[:]
l2.append(100)
l3.append(200)
print(l1)
print(l2)
print(l3)
l4=l1
