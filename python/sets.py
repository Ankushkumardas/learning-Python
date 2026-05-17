# sets do not allow duplicates and no indexing and no mutable data types and it itself is a mutable data type no 2d 3d sets are possible inside a set  and we use {} to make a set inside set we can have tuples but not lists or sets and uses hashing internally as not order or data is maintained  no concatination using + sign in sets 


# a=set()
# print(a)
# print(type(a))

a={1,1,12,3,4,6,7,8,765,4,32,4,67}
b={23,4,5,6,7,8,8}
print(a)
print(type(a))
# accessing -no
# adding items
a.add(22)
print(a)

# for deletion del, remove, pop

# fucntions of sets -->
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.isdisjoint(b))
print(a.issubset(b))
print(a.issuperset(b))