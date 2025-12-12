# app/routers/items.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..db import prisma
from ..models import ItemCreate, ItemRead

router = APIRouter()

from fastapi import APIRouter, HTTPException
from typing import List
from ..db import prisma
from ..models import ItemCreate, ItemRead, ItemUpdate

router = APIRouter()

# CREATE
@router.post("/", response_model=ItemRead)
async def create_item(payload: ItemCreate):
    # Verifica se a lista existe
    shopping_list = await prisma.shoppinglist.find_unique(where={"id": payload.shopping_list_id})
    if not shopping_list:
        raise HTTPException(status_code=404, detail="Shopping list not found")

    item = await prisma.item.create(
        data={
            "name": payload.name,
            "quantity": payload.quantity,
            "shoppingListId": payload.shopping_list_id
        }
    )
    return ItemRead(
        id=item.id,
        name=item.name,
        quantity=item.quantity,
        checked=item.checked,
        shopping_list_id=item.shoppingListId
    )

# READ ALL
@router.get("/", response_model=List[ItemRead])
async def get_items():
    items = await prisma.item.find_many()
    return [
        ItemRead(
            id=i.id,
            name=i.name,
            quantity=i.quantity,
            checked=i.checked,
            shopping_list_id=i.shoppingListId
        )
        for i in items
    ]

# READ ONE
@router.get("/{item_id}", response_model=ItemRead)
async def get_item(item_id: int):
    item = await prisma.item.find_unique(where={"id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemRead(
        id=item.id,
        name=item.name,
        quantity=item.quantity,
        checked=item.checked,
        shopping_list_id=item.shoppingListId
    )

# UPDATE
@router.put("/{item_id}", response_model=ItemRead)
async def update_item(item_id: int, payload: ItemUpdate):
    item = await prisma.item.find_unique(where={"id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    data = {}
    if payload.name is not None:
        data["name"] = payload.name
    if payload.quantity is not None:
        data["quantity"] = payload.quantity
    if payload.checked is not None:
        data["checked"] = payload.checked

    updated_item = await prisma.item.update(
        where={"id": item_id},
        data=data
    )

    return ItemRead(
        id=updated_item.id,
        name=updated_item.name,
        quantity=updated_item.quantity,
        checked=updated_item.checked,
        shopping_list_id=updated_item.shoppingListId
    )

# DELETE
@router.delete("/{item_id}", response_model=ItemRead)
async def delete_item(item_id: int):
    item = await prisma.item.find_unique(where={"id": item_id})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item = await prisma.item.delete(where={"id": item_id})
    return ItemRead(
        id=deleted_item.id,
        name=deleted_item.name,
        quantity=deleted_item.quantity,
        checked=deleted_item.checked,
        shopping_list_id=deleted_item.shoppingListId
    )

