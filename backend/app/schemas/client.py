from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import List, Optional

class ClientBase(BaseModel):
    name: str
    email: EmailStr

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    created_at: datetime
