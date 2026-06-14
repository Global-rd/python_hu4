from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import models, schemas

async def get_all_items(db: AsyncSession):
    result = await db.execute(select(models.Item))
    return result.scalars().all()

async def get_item_by_id(db: AsyncSession, item_id: str):
    result = await db.execute(select(models.Item).filter(models.Item.id == item_id))
    return result.scalars().first()

async def create_item(db: AsyncSession, item: schemas.ItemCreate):
    db_item = models.Item(
        item_name=item.item_name,
        quantity=item.quantity,
        price=item.price,
        category=item.category
    )
    db.add(db_item)
    await db.commit()
    await db.refresh(db_item)
    return db_item
'''
async def update_item(db: AsyncSession, db_item: models.Item, item_update: schemas.ItemUpdate):
    update_data = item_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_item, key, value)
    
    await db.commit()
    await db.refresh(db_item)
    return db_item
'''
#meghagytam a régi update_item-et, hogy látszódjon a különbség a formos és a sima update között, de most már a formos van használatban
async def update_item(db: AsyncSession, db_item: models.Item, item_update: schemas.ItemUpdate):
    # Az exclude_unset=True miatt csak azokat nézzük, amiket a formban átadtunk
    update_data = item_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        # EXTRA BIZTONSÁG: Csak akkor írjuk felül, ha a felhasználó tényleg beírt valami újat (nem None)
        if value is not None:
            setattr(db_item, key, value)
    
    await db.commit()
    await db.refresh(db_item)
    return db_item



async def delete_item(db: AsyncSession, db_item: models.Item):
    await db.delete(db_item)
    await db.commit()