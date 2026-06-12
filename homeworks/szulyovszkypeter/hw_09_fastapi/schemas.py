from pydantic import BaseModel, Field
from typing import Optional

class ItemBase(BaseModel):
    item_name: str = Field(..., min_length=1, max_length=100)
    quantity: int = Field(..., ge=0)
    price: float = Field(..., gt=0)
    category: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class ItemUpdate(BaseModel):
    item_name: Optional[str] = None
    quantity: Optional[int] = Field(None, ge=0)
    price: Optional[float] = Field(None, gt=0)
    category: Optional[str] = None

class ItemResponse(ItemBase):
    id: str # Az adatbázisból stringként kapjuk vissza a UUID-t

    class Config:
        # Ez teszi lehetővé, hogy a Pydantic beolvassa az ORM (SQLAlchemy) objektumokat
        from_attributes = True