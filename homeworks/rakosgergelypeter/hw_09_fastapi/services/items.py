
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from crud.items import (
    create_item,
    delete_item_by_id,
    get_all_items,
    get_item_by_id,
    update_item_by_id
)
from model import Items
from schemas import ItemsRequest

async def list_items_service(db: AsyncSession) -> list[Items]:
    return await get_all_items(db)

async def get_item_service(item_id: str, db: AsyncSession) -> Items:
    item = await get_item_by_id(item_id, db)

    if item is None:
        raise HTTPException(status_code=404, detail=f"Item id {movie_id} not found")
    
    return item

async def create_item_service(item: ItemsRequest, db:AsyncSession) -> Items:
    
    return await create_item(item, db)

async def update_movie_service(item_id: str, item_update: ItemsRequest, db:AsyncSession):
    item = await get_item_by_id(item_id, db)
    return await update_item_by_id(item, item_update, db)

async def delete_movie_service(item_id: str, db:AsyncSession):
    item = await get_item_service(item_id, db)
    return await delete_item_by_id(item, db)

