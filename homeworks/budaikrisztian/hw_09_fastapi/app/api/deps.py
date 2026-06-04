from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import AsyncSessionLocal
from app.repositories.product_repository import ProductRepository


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


DbSession = Annotated[AsyncSession, Depends(get_db)]


def get_product_repository(db: DbSession) -> ProductRepository:
    return ProductRepository(db)


ProductRepositoryDep = Annotated[
    ProductRepository,
    Depends(get_product_repository),
]
