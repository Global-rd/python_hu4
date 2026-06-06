from pydantic import BaseModel, Field


class ItemRequest(BaseModel):
    item_name: str = Field(min_length=1)
    quantity: int
    price: int
    category: str | None = None


class ItemResponse(ItemRequest):
    id: str