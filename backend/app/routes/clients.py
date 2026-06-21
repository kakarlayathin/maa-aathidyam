from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.client import Client as ClientModel
from app.schemas.client import Client, ClientCreate

router = APIRouter(prefix="/clients", tags=["clients"])

@router.post("/", response_model=Client)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = ClientModel(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.get("/", response_model=List[Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = db.query(ClientModel).offset(skip).limit(limit).all()
    return clients
