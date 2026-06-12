from typing import Optional

class ProductModel:
    def __init__(self, id: str, item_name: str, quantity: int, price: int, category: Optional[str] = None):
        self.id = id
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.category = category
