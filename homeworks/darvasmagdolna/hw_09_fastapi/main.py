from fastapi import FastAPI, HTTPException
from uuid import uuid1
from models import Item
from shemas import ItemCreate, ItemUpdate
from database import items

app = FastAPI()


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: str):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items")
def create_item(data: ItemCreate):
    new_item = Item(
        id=str(uuid1()),
        item_name=data.item_name,
        quantity=data.quantity,
        price=data.price,
        category=data.category
    )
    items.append(new_item)
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: str, data: ItemUpdate):
    for item in items:
        if item.id == item_id:
            if data.item_name is not None:
                item.item_name = data.item_name
            if data.quantity is not None:
                item.quantity = data.quantity
            if data.price is not None:
                item.price = data.price
            if data.category is not None:
                item.category = data.category
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    for item in items:
        if item.id == item_id:
            items.remove(item)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")