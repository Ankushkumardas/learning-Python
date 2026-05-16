# what are lists in python? can be compared to array in js  
# lists are mutable and ordered collection of items

# how different from arrays?

# 1. lists can hold different data types
# 2. list in python are mutable in nature but strings in python are immutable 
a=['sd','dfs','dgsd']
# print(type(a))
# print(a)
# b=['sfas',433,4.5]
# print(b)

# # 2d list
# c=['sdfa',422,['sf','fe',34]]
# print(c)

# d=list(['af',34,66.5])
# print(d)
# print(c[2][2])

# a[0]=324
# a[1:3]=[323,53]
# print(a)

# to add elemets to list -> append- to addd in last of list,extend - adds elements from another list  ,insert - to add element at specific index
# a.append('sef')
# a.extend(['fs',454,'dd'])
# # a.insert(1,'dcsc')
# print(a)
# a.insert(1,"new")
# print(a)

# deletion of elements from list -> del - delete at specific index , remove - delete at first occurrence of item ,pop - remove element at specific index (by default last ) ,clear - remove all items
# del a[2]
# print(a)
# a.remove("new")
# print(a)
# a.pop()
# print(a)
# a.clear()
# print(a)

# functions that are present on list -->
# list.sorted will make a new list and make chnages to that but list.sort will make chnages to that list only 

b="how are you"
print(b.capitalize())
print(b.split())
for i in b.split():
    # print(i.capitalize(),end="")
    print(i.capitalize())
    