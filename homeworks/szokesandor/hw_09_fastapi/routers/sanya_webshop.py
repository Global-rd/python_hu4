from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import WebshopItem
from schemas import AddWebshopItemRequest, UpdateWebshopItemRequest, WebshopItemResponse
import services.sanya_webshop as sv

router = APIRouter(prefix="/items", tags=["items"])

# Az összes webshop item lekérdezése
@router.get("/", response_model=list[WebshopItemResponse])
async def get_all_webshop_items(db: AsyncSession = Depends(get_db)) -> list[WebshopItem] | None:
    webshop_items = await sv.get_all_webshop_items_service(db)
    return webshop_items

# Egy webshop item lekérdezése ID alapján
@router.get("/{webshop_item_id}", response_model=WebshopItemResponse)
async def get_webshop_item(webshop_item_id: str, db:AsyncSession = Depends(get_db)) -> WebshopItem | None:
    webshop_item = await sv.get_webshop_item_service(webshop_item_id, db)
    return webshop_item

# Új webshop item hozzáadása a nyilvántartáshoz
@router.post("/", response_model=WebshopItemResponse)
async def add_webshop_item(item_to_add: AddWebshopItemRequest, db:AsyncSession = Depends(get_db)) -> WebshopItem:
    webshop_item = await sv.add_webshop_item_service(item_to_add, db)
    return webshop_item

# Nyilvántartásban lévő webshop item módosítása ID alapján
@router.put("/{webshop_item_id}", response_model=WebshopItemResponse)
async def update_webshop_item(webshop_item_id: str, item_update: UpdateWebshopItemRequest, db:AsyncSession = Depends(get_db)) -> WebshopItem:
    webshop_item = await sv.update_webshop_item_service(webshop_item_id, item_update, db)
    return webshop_item

# Nyilvántartásban lévő webshop item törlése ID alapján
@router.delete("/{webshop_item_id}", response_model=WebshopItemResponse)
async def delete_webshop_item(webshop_item_id: str, db:AsyncSession = Depends(get_db)) -> WebshopItem:
    webshop_item = await sv.delete_webshop_item_service(webshop_item_id, db)
    return webshop_item
