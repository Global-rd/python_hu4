from pydantic import BaseModel, Field

# Új tétel felviteléhez használható séma. Ebben az esetben a kategória kivételével minden mező kötelező.
class AddWebshopItemRequest(BaseModel):
    item_name: str = Field(..., min_length=1)
    quantity: int = Field(..., gt=0)
    price: int = Field(..., gt=0)
    category: str | None = None

# Tétel módosításhoz használható séma. Ebben az esetben a mezők elhagyhatók. Ha azonban egy mezőt megadnak, akkor annak  értéke - a kategória kivételével - nem lehet null.
class UpdateWebshopItemRequest(BaseModel):
    item_name: str = Field(default=None, min_length=1)
    quantity: int = Field(default=None, gt=0)
    price: int = Field(default=None, gt=0)
    category: str | None = Field(default=None, min_length=1)

# Válasz küldéséhez használható séma
class WebshopItemResponse(AddWebshopItemRequest):
    id: str
