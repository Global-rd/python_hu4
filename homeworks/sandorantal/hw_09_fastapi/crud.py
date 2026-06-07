from sqlalchemy.orm import Session
import models, schemas

def get_products(db: Session):
    return db.query(models.ProductModel).all()

def get_product_by_id(db: Session, product_id: str):
    return db.query(models.ProductModel).filter(models.ProductModel.id == product_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: str, updated_data: schemas.ProductBase):
    db_product = get_product_by_id(db, product_id)
    if db_product:
        db_product.item_name = updated_data.item_name
        db_product.quantity = updated_data.quantity
        db_product.price = updated_data.price
        db_product.category = updated_data.category
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: str):
    db_product = get_product_by_id(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
        return True
    return False