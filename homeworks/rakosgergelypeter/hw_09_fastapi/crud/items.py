from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import ItemsRequest

from model import Items

async def get_all_items(db: AsyncSession):
    result = await db.execute(select(Items)) # SELECT * FROM items
    items = list(result.scalars().all())
    return items

async def get_item_by_id(item_id: str, db:AsyncSession) -> Items | None:
    
    result = await db.execute(select(Items).where(Items.id == item_id))
    item = result.scalar_one_or_none()
    return item

async def create_item(item: ItemsRequest, db:AsyncSession) -> Items:
    new_item = Items(**item.model_dump())
    db.add(new_item)
    await db.commit()
    await db.refresh(new_item)

    return new_item

async def update_item_by_id(existing_item: Items,
                             item_update: ItemsRequest,
                             db: AsyncSession) -> Items:
    
    for key,value in item_update.model_dump(exclude_unset=True).items():
        setattr(existing_item, key, value)

    db.add(existing_item)
    await db.commit()
    await db.refresh(existing_item)
    return existing_item
    
async def delete_movie_by_id(item: Items, db:AsyncSession) -> Items:
    await db.delete(item)
    await db.commit()
    
    return item

