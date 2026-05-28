import pytest
from bank_account import BankAccount

@pytest.fixture
def empty_account():
    return BankAccount("Teszt Elek", 0)

@pytest.fixture
def funded_account():
    return BankAccount("Pelda Bela", 1000)

def test_initial_balance(funded_account):
    assert funded_account.get_balance() == 1000

@pytest.mark.parametrize("amount", [0, -50, -1.5])
def test_deposit_invalid_amounts(empty_account, amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        empty_account.deposit(amount)

def test_withdraw_insufficient_funds(funded_account):
    with pytest.raises(ValueError, match="Insufficient funds."):
        funded_account.withdraw(1500)

def test_transfer_to_non_account(funded_account):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        funded_account.transfer(100, "Not bankaccount")

def test_transfer_success(funded_account, empty_account):
    funded_account.transfer(400, empty_account)
    assert funded_account.get_balance() == 600
    assert empty_account.get_balance() == 400

def test_transfer_to_self(funded_account):
    with pytest.raises(ValueError, match="Cannot transfer money to the same account."):
        funded_account.transfer(100, funded_account)