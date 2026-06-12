from pydantic import BaseModel, Field

class ItemsRequest(BaseModel):
    item_name: str = Field(..., min_length=1) 
    quantity: str
    price: int
    category:str

class ItemsResponse(ItemsRequest):

    id: str
