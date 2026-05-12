

class ShoppingCart:

    def __init__(self):
        self.items = {}

    def add_item(self, item_name: str, price: float, quantity: int=1):

        if quantity <= 0:
            raise ValueError("Quantity must be positive!")
        if price < 0:
            raise ValueError("Price can not be negative!")
        
        if item_name in self.items:
            self.items[item_name]["quantity"] += quantity
        else:
            self.items[item_name] = {"price": price, "quantity": quantity}

    def remove_item(self):
        pass

    def get_total_cost(self):

        return sum(item["price"] * item["quantity"] for item in self.items.values())

    def get_discount_multiplier(self, discount_code:str) -> float:
        
        # in prod there would be adatabase call to check if discount code is valid
        valid_codes = {"SAVE10": 0.1, "SAVE20": 0.2}
        discount = valid_codes.get(discount_code, 0)
        return discount

    def checkout(self, discount_code: str) -> int:

        if not self.items:
            return 0
        discounted_price = self.get_total_cost() * (1 - self.get_discount_multiplier(discount_code))
        return discounted_price

