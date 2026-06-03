from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductRepository:
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_all(self) -> list[Product]:
        result = await self.db.execute(select(Product))
        return list(result.scalars().all())

    async def get_by_id(self, product_id: str) -> Product | None:
        result = await self.db.execute(
            select(Product).where(Product.id == product_id)
        )
        return result.scalar_one_or_none()

    async def create(self, product_data: ProductCreate) -> Product:
        product = Product(**product_data.model_dump())

        self.db.add(product)
        await self.db.commit()
        await self.db.refresh(product)

        return product

    async def update(
        self,
        product_id: str,
        product_data: ProductUpdate,
    ) -> Product | None:
        product = await self.get_by_id(product_id)

        if product is None:
            return None

        update_data = product_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(product, field, value)

        await self.db.commit()
        await self.db.refresh(product)

        return product

    async def delete(self, product_id: str) -> bool:
        product = await self.get_by_id(product_id)

        if product is None:
            return False

        await self.db.delete(product)
        await self.db.commit()

        return True
