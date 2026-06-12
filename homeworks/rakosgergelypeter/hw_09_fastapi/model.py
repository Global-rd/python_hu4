from uuid import uuid1
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Items(Base):

    __tablename__ = "items"

    """
    id (egyedi azonosító, pl uuid1 által generált)
    item_name (pl: morzsaporszívó)
    quantity (pl: 12)
    price (pl: 24900)
    category (ez a field legyen opcionális, pl: háztartási gép)
    """

    id: Mapped[str] = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name: Mapped[str] = mapped_column(String, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    category: Mapped[str] = mapped_column(Integer, nullable=True)

