from pydantic import BaseModel
from typing import Optional


class ItemCreate(BaseModel):
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None


class ItemUpdate(BaseModel):
    item_name: Optional[str] = None
    quantity: Optional[int] = None
    price: Optional[float] = None
    category: Optional[str] = None


class ItemResponse(BaseModel):
    id: str
    item_name: str
    quantity: int
    price: float
    category: Optional[str] = None

    model_config = {"from_attributes": True}
    