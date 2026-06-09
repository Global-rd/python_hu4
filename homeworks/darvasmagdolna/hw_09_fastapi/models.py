from pydantic import BaseModel
from uuid import uuid1


class Item(BaseModel):
    id: str = str(uuid1())
    item_name: str
    quantity: int
    price: int
    category: str
    