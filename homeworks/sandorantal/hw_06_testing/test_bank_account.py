import pytest
from bank_account import BankAccount

@pytest.fixture
def empty_account():
    return BankAccount(balance=0)

@pytest.fixture
def wealthy_account():
    return BankAccount(balance=1000)

@pytest.mark.parametrize("amount", [0, -50, -100])
def test_deposit_invalid_amounts(empty_account, amount):
    with pytest.raises(ValueError):
        empty_account.deposit(amount)

def test_withdraw_more_than_balance(wealthy_account):
    with pytest.raises(ValueError):
        wealthy_account.withdraw(2000)

def test_transfer_to_non_account(wealthy_account):
    invalid_recipient = "Not an account object"
    with pytest.raises(TypeError):
        wealthy_account.transfer(invalid_recipient, 100)

def test_initial_balance(wealthy_account):
    assert wealthy_account.balance == 1000