"""
database.py
-----------
Az adatbázis-kapcsolat boilerplate kódja (17. óra):
- async engine az aszinkron SQLite kapcsolathoz,
- session factory, ami minden request-hez külön session-t ad,
- Base, amitől minden adatbázis-modell örököl,
- get_db generator, ami a Depends-szel adja át a session-t.
"""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

# Melyik adatbázissal kommunikálunk. Más adatbázishoz szinte csak ezt írnánk át.
DATABASE_URL = "sqlite+aiosqlite:///./webshop.db"

# Az engine az adatbázis központi kezelője. Az echo=True miatt minden
# SQL parancs látszik a terminálban (pl. a CREATE TABLE az első induláskor).
engine = create_async_engine(DATABASE_URL, echo=True)

# Factory function: minden request-hez külön session-t gyárt.
# Az expire_on_commit=False kell, hogy commit után is vissza tudjuk adni
# a teljes objektumot (pl. a generált id-val) válaszként.
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    """Minden adatbázis-modell ettől az alapmodelltől örököl."""
    pass


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Minden request saját session-t kap. A yield átadja a session-t, a
    context manager pedig a request végén automatikusan lezárja.
    """
    async with AsyncSessionLocal() as session:
        yield session