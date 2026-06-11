from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from schema import ItemsRequest, ItemsResponse
from model import Items
from services.items import(
    create_item_service,
    delete_item_service,
    list_items_service,
    get_item_service,
    update_item_service
)

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)
@router.get("/", response_model=list[ItemsResponse])
async def get_items(db: AsyncSession = Depends(get_db)) -> list[Items]:

    return await list_items_service(db)

@router.post("/", response_model=ItemsResponse)
async def add_item(item: ItemsRequest, db: AsyncSession = Depends(get_db)) -> Items:

    return await create_item_service(item, db)

@router.get("/{item_id}", response_model=ItemsResponse)
async def get_movie(item_id: str, db:AsyncSession = Depends(get_db)) -> Items:
    return await get_item_service(item_id, db)


@router.put("/{item_id}", response_model=ItemsResponse)
async def update_item(
    item_id:str,
    item_update: ItemsRequest,
    db:AsyncSession = Depends(get_db)) -> Items:
    return await update_item_service(item_id, item_update, db)

@router.delete("/{item_id}", response_model=ItemsResponse)
async def delete_item(item_id:str, db:AsyncSession = Depends(get_db)) -> Items:
    return await delete_item_service(item_id, db)