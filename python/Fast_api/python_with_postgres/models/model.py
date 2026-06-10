from sqlalchemy import Boolean
from sqlalchemy import String
from uuid import uuid4
from sqlalchemy import true
from sqlalchemy import Column
from uuid import UUID
from config.db import Base,DEFAULT_SCHEMA_NAME

class TodoModel(Base):
    __tablename__="todo"
    __table_args__={"schema":DEFAULT_SCHEMA_NAME}
    
    id: UUID = Column(UUID(as_uuid=true),default=uuid4,primary_key=True,index==True)
    name:str =Column(
        String(200),
        nullable=False,
        index=True
    )
    category:str= Column(
        String(200),
        nullable=True,
        index=True
    )
    status:bool =Column(
        Boolean,
        default=False,
        nullable=False,
        index=True
    )