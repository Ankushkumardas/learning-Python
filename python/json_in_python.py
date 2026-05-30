# json are similar to pyth dictornary --> used in web development
# to use json in python you need to import a module json to use it 

import json
# a dict
a={
    "name": "john",
    "age": 30,
    "city": "new york"
}

print(a)
print(type(a))

# convert to json --> dumps method is used to convert a dicct to json 
a=json.dumps(a)
print(type(a))
print(a)

# convert json to python dict 
b=json.loads(a)
print(type(b))
print(b)