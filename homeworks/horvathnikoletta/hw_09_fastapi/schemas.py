from pydantic import BaseModel, Field

class ProductRequest(BaseModel):
    item_name: str = Field(..., min_length=1)
    quantity: int = Field(..., ge=0)
    price: int = Field(..., ge=0)

class ProductResponse(ProductRequest):
    id: str