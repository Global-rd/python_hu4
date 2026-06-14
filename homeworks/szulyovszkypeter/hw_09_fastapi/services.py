from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
import crud, schemas

async def fetch_all_items(db: AsyncSession):
    return await crud.get_all_items(db)

async def fetch_item_by_id(db: AsyncSession, item_id: str):
    db_item = await crud.get_item_by_id(db, item_id)
    if not db_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Termék nem található ezzel az azonosítóval: {item_id}"
        )
    return db_item

async def add_new_item(db: AsyncSession, item: schemas.ItemCreate):
    return await crud.create_item(db, item)

async def modify_item(db: AsyncSession, item_id: str, item_update: schemas.ItemUpdate):
    db_item = await fetch_item_by_id(db, item_id)
    return await crud.update_item(db, db_item, item_update)

async def remove_item(db: AsyncSession, item_id: str):
    db_item = await fetch_item_by_id(db, item_id)
    await crud.delete_item(db, db_item)