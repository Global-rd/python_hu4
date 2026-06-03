from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from models import WebshopItem
from schemas import AddWebshopItemRequest, UpdateWebshopItemRequest
import crud.sanya_webshop as crud

# Az összes webshop item lekérdezése
async def get_all_webshop_items_service(db: AsyncSession) -> list[WebshopItem] | None:
    webshop_items = await crud.get_all_webshop_items(db)
    return webshop_items

# Egy webshop item lekérdezése ID alapján
async def get_webshop_item_service(webshop_item_id: str, db: AsyncSession) -> WebshopItem | None:
    webshop_item = await crud.get_webshop_item(webshop_item_id, db)
    if webshop_item is None:
        raise HTTPException(status_code=404, detail=f"Item id {webshop_item_id} not found!")
    return webshop_item

# Új webshop item hozzáadása a nyilvántartáshoz
async def add_webshop_item_service(item_to_add: AddWebshopItemRequest, db:AsyncSession) -> WebshopItem:
    webshop_item = await crud.add_webshop_item(item_to_add, db)
    return webshop_item

# Nyilvántartásban lévő webshop item módosítása ID alapján
async def update_webshop_item_service(webshop_item_id: str, item_update: UpdateWebshopItemRequest, db:AsyncSession) -> WebshopItem:
    webshop_item = await get_webshop_item_service(webshop_item_id, db)
    webshop_item = await crud.update_webshop_item(webshop_item, item_update, db)
    return webshop_item

# Nyilvántartásban lévő webshop item törlése ID alapján
async def delete_webshop_item_service(webshop_item_id: str, db:AsyncSession) -> WebshopItem:
    webshop_item = await get_webshop_item_service(webshop_item_id, db)
    webshop_item = await crud.delete_webshop_item(webshop_item, db)
    return webshop_item
