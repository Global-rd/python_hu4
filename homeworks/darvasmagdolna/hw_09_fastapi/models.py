from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import mapped_column
from uuid import uuid1
from database import Base


class Item(Base):
    __tablename__ = "items"

    id = mapped_column(String, primary_key=True, default=lambda: str(uuid1()))
    item_name = mapped_column(String, nullable=False)
    quantity = mapped_column(Integer, nullable=False)
    price = mapped_column(Integer, nullable=False)
    category = mapped_column(String, nullable=True)
    