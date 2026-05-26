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
l=[1,2,3,4,5,6,7,8,9,10]
a=map(lambda x:x**2,l)
# print(a) --> you cannot directly view the map data you need to convert teh map in list and than you can view the data 
print(list(a))
