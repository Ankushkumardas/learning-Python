# request components-->
# type/method(GET/POST/PUT/DELETE),path/url,body,headers

# response components-->status code, body, headers

from requests import request
import requests

url='https://jsonplaceholder.typicode.com/todos'
params={"page":2}
# url='https://reqres.in/api/users'
res=requests.get(url,params=params)
print(res.url)
print(res.status_code)
print(res.headers.get("Content-Type"))
# print(res.raise_for_status())   used if we get a 40* or 50* error encountered

# print(res.json())
# print(res.headers)

# data=res.json()
# for i in data:
#     print(i["title"],end="\n")
