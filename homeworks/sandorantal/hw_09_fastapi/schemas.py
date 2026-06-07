from typing import Optional
from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    item_name: str = Field(..., example="crumb vacuum cleaner")
    quantity: int = Field(..., example=12)
    price: int = Field(..., example=24900)
    category: Optional[str] = Field(None, example="household appliance")

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: str

    class Config:
        from_attributes = True