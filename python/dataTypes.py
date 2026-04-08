# basic--> interger,float,complex,boolean,string
# container type-->{ List->like array,Tuple,Sets and Dictonary-> key value pairs}
# user defined-->Class

# list
print([1,2,3,4,5])
# tuple
print((1,2,3,4,5))
# sets
print({1,1,2,3,4,4,5})
# dictonary
print({1:"a",2:"b",3:"c",4:"d",5:"e"})


# variables-->
# dynamic typing--> in python we do not have to tell what type of data type we are using python is smart enough and automaticc  assign teh data type to teh value you have set 
# static typeing --> in all other languages we have to tell what type of data type we have to use 
#  and dynamic binding--> below we can see teh same a has been assigned to difefrnt data types but no error is shown thi sis called dynamci binding a variable which can store multiple data types
a="kajslkcn"
print(a)
a=343
print(a)
a=True
print(a)
print(type(a))
a=34;b="scj";c=True
print(a,b,c)
a,b,c=c,a,b
print(a,b,c)
a,b,c="jbsc",False,353
print(a,b,c)