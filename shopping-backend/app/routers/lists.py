# app/routers/lists.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..db import prisma
from pydantic import BaseModel
from ..models import ListCreate, ListRead

router = APIRouter()


# CREATE
@router.post("/", response_model=ListRead)
async def create_list(payload: ListCreate):
    shopping_list = await prisma.shoppinglist.create(
        data={"title": payload.title}
    )
    return ListRead(id=shopping_list.id, title=shopping_list.title)

# READ ALL
@router.get("/")
async def get_lists():
    lists = await prisma.shoppinglist.find_many(
        include={
            "items": True
        }
    )

    print("LISTS BACKEND:", lists)

    result = []
    for lst in lists:
        result.append({
            "id": lst.id,
            "title": lst.title,
            "createdAt": lst.createdAt,
            "itemsCount": len(lst.items),
        })

    return result  # ⬅️ ISSO É CRÍTICO
# READ ONE
@router.get("/{list_id}", response_model=ListRead)
async def get_list(list_id: int):
    lst = await prisma.shoppinglist.find_unique(
        where={"id": list_id},
        include={"items": True}
    )

    if not lst:
        raise HTTPException(status_code=404, detail="Shopping list not found")

    return ListRead(
        id=lst.id,
        title=lst.title,
        createdAt=lst.createdAt.isoformat(),
        itemsCount=len(lst.items)
    )

# UPDATE
@router.put("/{list_id}", response_model=ListRead)
async def update_list(list_id: int, payload: ListCreate):
    shopping_list = await prisma.shoppinglist.update(
        where={"id": list_id},
        data={"title": payload.title}
    )
    return ListRead(id=shopping_list.id, title=shopping_list.title)

# DELETE
@router.delete("/{list_id}", response_model=ListRead)
async def delete_list(list_id: int):
    shopping_list = await prisma.shoppinglist.delete(where={"id": list_id})
    return ListRead(id=shopping_list.id, title=shopping_list.title)
