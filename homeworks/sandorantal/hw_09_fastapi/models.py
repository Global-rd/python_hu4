import uuid
from sqlalchemy import Column, String, Integer
from database import Base

def generate_uuid():
    return str(uuid.uuid1())

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    item_name = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    category = Column(String, nullable=True)