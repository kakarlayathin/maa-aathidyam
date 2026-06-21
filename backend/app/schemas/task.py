from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional
from app.models.task import TaskStatus

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.backlog
    project_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
