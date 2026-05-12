import pytest
from shopping_cart import ShoppingCart
from unittest.mock import patch

#FIXTURE
@pytest.fixture
def empty_cart():
    return ShoppingCart()


@pytest.fixture
def cart_with_items():
    cart = ShoppingCart()
    cart.add_item("apple", 1, 3)
    cart.add_item("pear", 2, 4)
    return cart


def test_add_item_changed_quantity(empty_cart):
    
    empty_cart.add_item("apple", 1, 3)
    assert empty_cart.items["apple"]["quantity"] == 3


def test_add_item_did_not_affect_price(empty_cart):
    
    empty_cart.add_item("apple", 1, 3)
    assert empty_cart.items["apple"]["price"] == 1


@pytest.mark.parametrize("item_name, price, quantity, expected_exception", [
    ("orange", -1, 1, ValueError), # negative price
    ("orange", 1, 0, ValueError), # zero quantity
    ("orange", 1, -1, ValueError), # negative quantity
])
def test_add_item_with_invalid_input(empty_cart, item_name, price, quantity, expected_exception):
    with pytest.raises(expected_exception):
        empty_cart.add_item(item_name, price, quantity)

@patch('shopping_cart.ShoppingCart.get_discount_multiplier', return_value=0.1)
def test_checkout(mock_apply_discount, cart_with_items):
    final_price = cart_with_items.checkout("SAVE10")
    assert final_price == 9.9
    mock_apply_discount.assert_called_once_with("SAVE10")


#mocking: új, kitalált objektum ami egy előre beállított értéket ad vissza a teszt során, ez lesz a mock_apply_discount
#patching: egy létező függvény hívását lecseréljük egy mockolt verzióra