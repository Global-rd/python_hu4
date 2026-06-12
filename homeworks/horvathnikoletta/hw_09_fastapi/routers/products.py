from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import Product
from schemas import ProductRequest, ProductResponse
from services.products import (
    create_product_service,
    delete_product_service,
    update_product_service,
    list_products_service,
    get_product_service
)

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("/", response_model=list[ProductResponse])
async def get_products(db: AsyncSession = Depends(get_db)) -> list[Product]:
    return await list_products_service(db)

@router.post("/", response_model=ProductResponse)
async def add_product(product: ProductRequest, db: AsyncSession = Depends(get_db)) -> Product:
    return await create_product_service(product, db)

@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str, db: AsyncSession = Depends(get_db)) -> Product:
    return await get_product_service(product_id, db)

@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: str,
    product_update: ProductRequest,
    db: AsyncSession = Depends(get_db)
) -> Product:
    return await update_product_service(product_id, product_update, db)

@router.delete("/{product_id}", response_model=ProductResponse)
async def delete_product(product_id: str, db: AsyncSession = Depends(get_db)) -> Product:
    return await delete_product_service(product_id, db)