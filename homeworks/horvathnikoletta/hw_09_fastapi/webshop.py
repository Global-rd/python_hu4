from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uuid

app = FastAPI()

products_db = [
    {
        "id": "12345",
        "item_name": "robotporszívó",
        "quantity": 20,
        "price": 79900,
        "category": "haztartasi gep"
    }
]

class Product(BaseModel):
    id: str
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

class ProductIn(BaseModel):
    item_name: str
    quantity: int
    price: int
    category: Optional[str] = None

@app.get("/products", response_model=List[Product])
def get_all_products():
    return products_db

@app.get("/products/{product_id}", response_model=Product)
def get_one_product(product_id: str):
    for p in products_db:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/products", response_model=Product)
def add_product(product: ProductIn): 
    generated_id = str(uuid.uuid1())
    
    new_product = {
        "id": generated_id,
        "item_name": product.item_name,
        "quantity": product.quantity,
        "price": product.price,
        "category": product.category
    }
    products_db.append(new_product)
    return new_product

@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: str, product: ProductIn): 
    for p in products_db:
        if p["id"] == product_id:
            p["item_name"] = product.item_name
            p["quantity"] = product.quantity
            p["price"] = product.price
            p["category"] = product.category
            return p
            
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    for i, p in enumerate(products_db):
        if p["id"] == product_id:
            products_db.pop(i)
            return {"message": "Item deleted successfully"}
            
    raise HTTPException(status_code=404, detail="Item not found")