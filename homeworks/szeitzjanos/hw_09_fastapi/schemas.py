from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: str
