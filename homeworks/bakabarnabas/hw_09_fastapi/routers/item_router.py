from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from db.database import get_db
from schemas.item import ItemCreate, ItemUpdate, ItemResponse
import services.item_service as item_service

router = APIRouter(prefix="/items", tags=["items"])


@router.get("", response_model=list[ItemResponse])
def list_items(db: Session = Depends(get_db)):
    """Minden termék listázása."""
    return item_service.get_all_items(db)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: str, db: Session = Depends(get_db)):
    """1 termék lekérése id alapján."""
    return item_service.get_item_by_id(db, item_id)


@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    """1 termék hozzáadása (id automatikusan generálódik)."""
    return item_service.create_item(db, item)


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: str, item: ItemUpdate, db: Session = Depends(get_db)):
    """1 termék adatainak frissítése id alapján."""
    return item_service.update_item(db, item_id, item)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: str, db: Session = Depends(get_db)):
    """1 termék törlése id alapján."""
    item_service.delete_item(db, item_id)
    