# we make a pydentic responce model like 
from itertools import count
from fastapi import APIRouter, status, HTTPException,Response,Request
from pydantic import Field, BaseModel
from uuid import uuid4, UUID

router = APIRouter(prefix="/todo")

class TodoCreate(BaseModel):
    name: str
    cat: str
    status: bool = False

class Todo(BaseModel):
    # UUID gives teh type of teh uuid 
    id: UUID = Field(default_factory=uuid4)
    name: str
    cat: str
    status: bool = False

class TodoOut(BaseModel):
    todo: Todo
    msg: str
# we create a vrialbe to stroe all our data called db which is of list of todo type adn is empoty now 
db: list[Todo] = []


@router.post("/create")
def create_todo(data: TodoCreate):
    new_todo = Todo(
        name=data.name,
        cat=data.cat,
        status=data.status
    )
    db.append(new_todo)
    return TodoOut(todo=new_todo, msg="Data added sucecssfully")

class TodogetOut(BaseModel):
    todo: list[Todo]
    msg: str
    api_count=int
    
@router.get("/")
def get_data(Request:Request):
    return TodogetOut(todo=db, msg="All todo data",api_count=Request.app.state.count)

@router.get("/{id}")
def get_todo_byId(id: UUID):
    for todo in db:
        if todo.id == id:
            return TodoOut(todo=todo, msg=f"This todo of id {id}")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    