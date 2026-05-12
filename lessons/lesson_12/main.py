from cart_processor import process_cart_items

def main() -> None:

    shopping_cart = {
        "Timmy": [10,6,7,4,5],
        "John": [1,2,3],
        "Alice": [1,2,3,6,9]
    }

    for customer, prices in shopping_cart.items():
        process_cart_items(customer, prices)


if __name__ == "__main__":
    main()