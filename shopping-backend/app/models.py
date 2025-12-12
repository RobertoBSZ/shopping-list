# app/models.py
from pydantic import BaseModel
from typing import Optional

# Schemas
class ListCreate(BaseModel):
    title: str  # antes era name

class ListRead(BaseModel):
    id: int
    title: str  # antes era name

class ItemCreate(BaseModel):
    name: str
    quantity: Optional[int] = 1
    shopping_list_id: int

class ItemRead(BaseModel):
    id: int
    name: str
    quantity: int
    checked: bool
    shopping_list_id: int

class ItemUpdate(BaseModel):
    name: str | None = None
    quantity: int | None = None
    checked: bool | None = None
