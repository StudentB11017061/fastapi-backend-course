from pydantic import BaseModel

#Pydantic
class TodoBase(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False
    due_date: date | None = None
    priority: int | None = None

class TodoCreate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: int

    class Config:
        from_attributes = True
