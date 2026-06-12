from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from schemas import ItemRequest, ItemResponse
from services import (
    create_item_service,
    delete_item_service,
    get_item_service,
    list_items_service,
    update_item_service,
)

router = APIRouter(prefix="/items", tags=["items"])


@router.get("/", response_model=list[ItemResponse])
async def get_items(db: AsyncSession = Depends(get_db)):
    return await list_items_service(db)


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: str, db: AsyncSession = Depends(get_db)):
    return await get_item_service(item_id, db)


@router.post("/", response_model=ItemResponse)
async def add_item(item: ItemRequest, db: AsyncSession = Depends(get_db)):
    return await create_item_service(item, db)


@router.put("/{item_id}", response_model=ItemResponse)
async def update_item(item_id: str, item_update: ItemRequest, db: AsyncSession = Depends(get_db)):
    return await update_item_service(item_id, item_update, db)


@router.delete("/{item_id}", response_model=ItemResponse)
async def delete_item(item_id: str, db: AsyncSession = Depends(get_db)):
    return await delete_item_service(item_id, db)