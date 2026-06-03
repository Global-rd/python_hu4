import uuid
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Webshop Product Registry")


class ProductBase(BaseModel):
    item_name: str = Field(..., example="crumb vacuum cleaner")
    quantity: int = Field(..., example=12)
    price: int = Field(..., example=24900)
    category: Optional[str] = Field(None, example="household appliance")

class Product(ProductBase):
    id: str
 
db_products = {}


@app.get("/products", response_model=list[Product])
def get_all_products():
    return list(db_products.values())


@app.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: str):
    if product_id not in db_products:
        raise HTTPException(status_code=404, detail="Product not found.")
    return db_products[product_id]


# JAVÍTÁS: status_code átírva 21-ről 201-re
@app.post("/products", response_model=Product, status_code=201)
def create_product(product_data: ProductBase):
    # JAVÍTÁS: uuid4() átírva uuid1()-re a feladatleírás alapján
    generated_id = str(uuid.uuid1())
    
    new_product = Product(id=generated_id, **product_data.model_dump())
    
    db_products[generated_id] = new_product
    return new_product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: str, updated_data: ProductBase):
    if product_id not in db_products:
        raise HTTPException(status_code=404, detail="The product you are trying to update cannot be found..")
    
    updated_product = Product(id=product_id, **updated_data.model_dump())
    db_products[product_id] = updated_product
    return updated_product


@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    if product_id not in db_products:
        raise HTTPException(status_code=404, detail="The product you want to delete cannot be found..")
    
    del db_products[product_id]
    return {"message": f"Product with ID {product_id} has been successfully deleted.."}