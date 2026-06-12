from fastapi import FastAPI, HTTPException
from repository import ProductRepository
from schemas import Product, ProductCreate, ProductUpdate
from database import init_db

app = FastAPI()
repo = ProductRepository()

# SQLite database init
init_db()


@app.get('/products', response_model=list[Product])
def list_products():
    return repo.list_all()


@app.get('/products/{product_id}', response_model=Product)
def get_product(product_id: str):
    product = repo.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product


@app.post('/products', response_model=Product)
def create_product(data: ProductCreate):
    return repo.create(data)


@app.put('/products/{product_id}', response_model=Product)
def update_product(product_id: str, data: ProductUpdate):
    product = repo.update(product_id, data)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product


@app.delete('/products/{product_id}')
def delete_product(product_id: str):
    if not repo.delete(product_id):
        raise HTTPException(status_code=404, detail='Product not found')
    return {'message': 'Product deleted successfully'}
