def calculate_total(prices: list[int]) -> int:
    return sum(prices)


def process_cart_items(customer_name: str, prices: list[int]) -> int:

    total_price = calculate_total(prices)
    print(f"Total prices for {customer_name}: ${total_price}")
    return total_price