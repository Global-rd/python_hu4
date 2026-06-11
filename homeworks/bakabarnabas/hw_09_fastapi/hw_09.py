from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uuid

app = FastAPI(title="Webshop Termék Nyilvántartó")

# --- Adatbázis (in-memory dict) ---
db: dict[str, dict] = {}


# --- Modellek ---
class ItemCreate(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None


class ItemUpdate(BaseModel):
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    category: Optional[str] = None


class ItemResponse(BaseModel):
    id: str
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None


# --- Endpointok ---

@app.get("/items", response_model=list[ItemResponse])
def list_items():
    """Minden termék listázása."""
    return list(db.values())


@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: str):
    """1 termék listázása id alapján."""
    if item_id not in db:
        raise HTTPException(status_code=404, detail="A termék nem található.")
    return db[item_id]


@app.post("/items", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate):
    """1 termék hozzáadása (id automatikusan generálódik)."""
    item_id = str(uuid.uuid1())
    new_item = {"id": item_id, **item.model_dump()}
    db[item_id] = new_item
    return new_item


@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: str, item: ItemUpdate):
    """1 termék adatainak frissítése id alapján."""
    if item_id not in db:
        raise HTTPException(status_code=404, detail="A termék nem található.")
    updated_fields = item.model_dump(exclude_unset=True)
    db[item_id].update(updated_fields)
    return db[item_id]


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: str):
    """1 termék törlése id alapján."""
    if item_id not in db:
        raise HTTPException(status_code=404, detail="A termék nem található.")
    del db[item_id]