import pytest
from bank_account import BankAccount

# FIXTURES

@pytest.fixture
def bank_account_empty():
    return BankAccount(owner="Bumm")

@pytest.fixture
def bank_account_rich():
    return BankAccount(owner="Rich", balance=100)






def test_depositing(bank_account_empty):
    bank_account_empty.deposit(100)
    assert bank_account_empty.get_balance() == 100


def test_negative_value_of_deposit(bank_account_empty) -> None:
    with pytest.raises(
        ValueError, match = 'The amount must be positive!'
    ):
        (bank_account_empty).deposit(-5000)