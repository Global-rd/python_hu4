from pydantic import BaseModel, Field

class ItemsRequest(BaseModel):
    title: str = Field(..., min_length=1) 
    genre: str
    year: int
    length_in_mins:int
    rating:int = 0

class ItemsResponse(ItemsRequest):

    id: str
