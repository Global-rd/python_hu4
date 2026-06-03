from uuid import uuid1
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

# Az adatbázis egyetlen "webshop_items" nevű táblát tartalmaz, amelyben a kategória kivételével minden kötelező. Az egyedi azonosítót az uuid1 adja
class WebshopItem(Base):
    __tablename__ = "webshop_items"
    id: Mapped[str] = mapped_column(String, primary_key=True, nullable=False, default=lambda: str(uuid1()))
    item_name: Mapped[str] = mapped_column(String, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=True)
