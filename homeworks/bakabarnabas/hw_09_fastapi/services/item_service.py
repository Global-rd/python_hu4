from sqlalchemy.orm import Session
from fastapi import HTTPException

from models.item import Item
from schemas.item import ItemCreate, ItemUpdate


def get_all_items(db: Session) -> list[Item]:
    return db.query(Item).all()


def get_item_by_id(db: Session, item_id: str) -> Item:
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="A termék nem található.")
    return item


def create_item(db: Session, item_data: ItemCreate) -> Item:
    new_item = Item(**item_data.model_dump())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def update_item(db: Session, item_id: str, item_data: ItemUpdate) -> Item:
    item = get_item_by_id(db, item_id)
    updated_fields = item_data.model_dump(exclude_unset=True)
    for key, value in updated_fields.items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item


def delete_item(db: Session, item_id: str) -> None:
    item = get_item_by_id(db, item_id)
    db.delete(item)
    db.commit()