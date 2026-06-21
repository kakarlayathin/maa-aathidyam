from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.task import Task as TaskModel
from app.schemas.task import Task, TaskCreate

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    db_task = TaskModel(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.get("/", response_model=List[Task])
def read_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = db.query(TaskModel).offset(skip).limit(limit).all()
    return tasks
