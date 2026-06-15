from sqlalchemy import true
from sqlalchemy import func
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy import Boolean
from sqlalchemy import String
from uuid import uuid4
from uuid import UUID
from config.db import Base,DEFAULT_SCHEMA_NAME
from sqlalchemy.orm import Mapped,mapped_column

class TodoModel(Base):
    __tablename__="todo"
    __table_args__={"schema":DEFAULT_SCHEMA_NAME}
    
    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
        index=True
    )
    
    name:Mapped[str] =mapped_column(
        String(200),
        nullable=False,
        index=True
    )
    category:Mapped[str]= mapped_column(
        String(200),
        nullable=True,
        index=True
    )
    status:Mapped[bool] =mapped_column(
        Boolean,
        default=False,
        nullable=False,
        index=True
    )
    created_at:Mapped[datetime] =mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    updated_at:Mapped[datetime]= mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )