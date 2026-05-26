# dictonary has key value pairs --> we use {} to make dictonary
# rules --> it has no indexing , it is a mutable data type, keys shoudl be always immutable values can be mutable and keys should be unique
a={'name':'ank','age':22}
print(a)
print(type(a))

# access items from dcitornary 
print(a['name'])

# edit values from dcitornary
a['name']='hsacj'
print(a) 

# add new key value pair 
a["city"]="india"
print(a)  

# delete key vakue pair we use del and the key -
del a["city"]
print(a)

# for i in a:
#     print(i,a[i],end=" ")

print(a.keys())
print(a.values())


a={'name':'ank','age':22}
print(a.items())

for i,j in a.items():
    print(i,end=" ")
# in 