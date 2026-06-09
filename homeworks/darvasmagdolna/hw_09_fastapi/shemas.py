from pydantic import BaseModel


class ItemCreate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: str


class ItemUpdate(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: str
    