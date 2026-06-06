"""
models.py
---------
Az adatbázis-modell. Pythonban leírjuk, milyen tábla jöjjön létre az
SQLite-ban. A Base-től örököl, így a Base.metadata.create_all létrehozza
belőle a táblát az 5 oszloppal.
"""

from uuid import uuid1

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Item(Base):
    __tablename__ = "items"

    # Egyedi azonosító (primary key). A felhasználó nem adja meg, a tábla
    # generálja alapból uuid1 értékkel (a lambda egy névtelen, egysoros függvény).
    id: Mapped[str] = mapped_column(
        String, primary_key=True, default=lambda: str(uuid1())
    )

    # A termék neve, kötelező (nem lehet üres / hiányzó).
    item_name: Mapped[str] = mapped_column(String, nullable=False)

    # Mennyiség és ár egész számok, kötelezőek.
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)

    # A kategória OPCIONÁLIS, ezért lehet None (nullable=True).
    category: Mapped[str | None] = mapped_column(String, nullable=True)