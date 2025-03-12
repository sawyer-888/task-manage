from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str = ""
    priority: int
    deadline: str = ""
