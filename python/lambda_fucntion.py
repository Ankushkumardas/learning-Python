# lambda funtion are writte ina  single line and are mostly used in highher order functions and it has no return value and it return a fucntion

# a=lambda x,y: x+y
# print(a(1,2))

# a=lambda x:x[0]=='a' or x[0]=='A'
# print(a("Ankit"))

# a=lambda x:'even' if x%2==0 else 'odd'
# print(a(34233))

# def data(fun,l):
#     res=0
#     for i in l:
#         if fun(i):
#             res+=i
#     return res

# l=[23,3,4,5,6]

# x=lambda x:x%2!=0

# print(data(x,l))


# --->
# map fucntion : map(fucntion,iterable) --> fucntion will be a lambda fucntion
# l=[1,2,3,4,5,6,7,8,9,10]
# a=map(lambda x:x**2,l)
#// print(a) --> you cannot directly view the map data you need to convert teh map in list and than you can view the data 
# print(list(a))


from functools import reduce
a=[
    {"name":"Ankit","age":22,"salary":20000},
    {"name":"Mohit","age":24,"salary":40000},
    {"name":"Rahul","age":26,"salary":60000},
    {"name":"Anamika","age":28,"salary":80000},
]

# b=lambda x:x['age']>22
b=lambda x:x['name']
print(list(map(b,a)))

# filter funciton : filter(fucntion,iterable) --> fucntion will be a lambda fucntion --> it return the boolean value

c=lambda x:x['age']>=25
print(list(filter(c,a)))


d=lambda x:'i' in x["name"]
print(list(filter(d,a)))

import functools

a=reduce(lambda x,y:x+y,[1,23,4,5,6])
print(a)



# list comprehension --> [expression for item in iterable]
a=[1,2,3,4,5,6,7,8,9,10]

b=[x%2==0 for x in a]
print(b)


b=[x**2 for x in a if x%2==0]
print(b)