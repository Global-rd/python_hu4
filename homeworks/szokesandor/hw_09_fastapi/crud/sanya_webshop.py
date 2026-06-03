from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import WebshopItem
from schemas import AddWebshopItemRequest, UpdateWebshopItemRequest

# Az összes webshop item lekérdezése
async def get_all_webshop_items(db: AsyncSession) -> list[WebshopItem] | None:
    result = await db.execute(select(WebshopItem))
    webshop_items = list(result.scalars().all())
    return webshop_items

# Egy webshop item lekérdezése ID alapján
async def get_webshop_item(webshop_item_id: str, db:AsyncSession) -> WebshopItem | None:
    result = await db.execute(select(WebshopItem).where(WebshopItem.id == webshop_item_id))
    webshop_item = result.scalar_one_or_none()
    return webshop_item

# Új webshop item hozzáadása a nyilvántartáshoz
async def add_webshop_item(item_to_add: AddWebshopItemRequest, db:AsyncSession) -> WebshopItem:
    webshop_item = WebshopItem(**item_to_add.model_dump())
    db.add(webshop_item)
    await db.commit()
    await db.refresh(webshop_item)
    return webshop_item

# Nyilvántartásban lévő webshop item módosítása
async def update_webshop_item(webshop_item: WebshopItem, item_update: UpdateWebshopItemRequest, db: AsyncSession) -> WebshopItem:
    for key,value in item_update.model_dump(exclude_unset=True).items():
        setattr(webshop_item, key, value)
    db.add(webshop_item)
    await db.commit()
    await db.refresh(webshop_item)
    return webshop_item

# Nyilvántartásban lévő webshop item törlése
async def delete_webshop_item(webshop_item: WebshopItem, db:AsyncSession) -> WebshopItem:
    await db.delete(webshop_item)
    await db.commit()
    return webshop_item
