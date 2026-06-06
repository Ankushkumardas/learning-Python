# Think of learning them in this order: for Fast API

# 1. Validation
# 2. Response Models
# 3. Status Codes
# 4. Middleware
# 5. Dependency Injection
# 6. Authentication
# 7. JWT
# 8. OAuth
# 9. File Upload
# 10. Background Tasks
# 11. Streaming Responses
# 12. WebSockets
# <-------------------------------->

#1. for validation we did use pydentic 

#2. for responce model 
# so your db conatins your password in simple or hashed form but you donot want to show that so we do ->

# we make a pydentic responce model like 
from pydantic import Field
from pydantic import BaseModel
from fastapi import FastAPI, status, HTTPException
from uuid import uuid4, UUID
app=FastAPI()

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


@app.post("/create")
def create_todo(data: TodoCreate):
    new_todo = Todo(
        name=data.name,
        cat=data.cat,
        status=data.status
    )
    db.append(new_todo)
    return TodoOut(todo=new_todo, msg="Data added sucecssfully")

class TodogetOut(BaseModel):
    todo:list[Todo]
    msg:str
    
@app.get("/todos")
def get_data():
    return TodogetOut(todo=db,msg="All todo data")

@app.get("/todos/{id}")
def get_todo_byId(id: UUID):
    for todo in db:
        if todo.id == id:
            return TodoOut(todo=todo, msg=f"This todo of id {id}")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    