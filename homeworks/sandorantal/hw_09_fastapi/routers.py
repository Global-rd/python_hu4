from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schemas, crud

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("", response_model=list[schemas.Product])
def get_all_products(db: Session = Depends(get_db)):
    return crud.get_products(db)

@router.get("/{product_id}", response_model=schemas.Product)
def get_product_by_id(product_id: str, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found.")
    return db_product

@router.post("", response_model=schemas.Product, status_code=201)
def create_product(product_data: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product_data)

@router.put("/{product_id}", response_model=schemas.Product)
def update_product(product_id: str, updated_data: schemas.ProductBase, db: Session = Depends(get_db)):
    db_product = crud.update_product(db, product_id, updated_data)
    if not db_product:
        raise HTTPException(status_code=404, detail="The product you are trying to update cannot be found.")
    return db_product

@router.delete("/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    success = crud.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="The product you want to delete cannot be found.")
    return {"message": f"Product with ID {product_id} has been successfully deleted."}