from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models import Item
from shemas import ItemCreate, ItemUpdate
from database import get_db, engine, Base

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/items")
async def list_items(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item))
    return result.scalars().all()


@app.get("/items/{item_id}")
async def get_item(item_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalars().one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items")
async def create_item(data: ItemCreate, db: AsyncSession = Depends(get_db)):
    new_item = Item(**data.dict())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)
    return new_item


@app.put("/items/{item_id}")
async def update_item(item_id: str, data: ItemUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalars().one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in data.dict().items():
        setattr(item, key, value)

    await db.commit()
    await db.refresh(item)
    return item


@app.delete("/items/{item_id}")
async def delete_item(item_id: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalars().one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    await db.delete(item)
    await db.commit()
    return {"message": "Item deleted"}

