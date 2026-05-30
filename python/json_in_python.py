# # json are similar to pyth dictornary --> used in web development
# # to use json in python you need to import a module json to use it 

# import json
# # a dict
# a={
#     "name": "john",
#     "age": 30,
#     "city": "new york"
# }

# print(a)
# print(type(a))

# # convert to json --> dumps method is used to convert a dicct to json 
# a=json.dumps(a)
# print(type(a))
# print(a)

# # convert json to python dict 
# b=json.loads(a)
# print(type(b))
# print(b)


# when we talk about files we use json.load and json.dump
# to write into teh file -->
import json
a={
    "name": "john",
    "age": 30,
    "city": "new york"
}

with open('a.json','r') as file:
    # json.dump(a,file,indent=1)
    # print(json.load(file))
    data=json.load(file)
    print(data["name"])
    