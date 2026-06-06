from fastapi import APIRouter,Request,Response

router = APIRouter(prefix="/users")

@router.get("/")
def get_users(Request:Request,Response:Response):
    # print(Request.url)
    # print(Request.url_for)
    # data=Request.headers
    # for key,value in data.items():
    #     if key=="connection":
    #         print(f"{key}, {value}")
    # print(Response.status_code)
    
    Response.status_code=201
    print("after route")
    return [
        {"id": 1, "name": "test1"},
        {"id": 2, "name": "test2"},
        {"id": 3, "name": "test3"},
    ]