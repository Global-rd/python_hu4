import pytest
from bank_account import BankAccount

@pytest.fixture
def account_Bob():
    return BankAccount("Bob", 100)


@pytest.fixture
def account_Jhon():
    return BankAccount("Bob", 50.5)

@pytest.mark.parametrize("amount, expected", [
    (100, False),
    (0, True),
    (-10, True),

])

def test_deposit(account_Bob, amount, expected):
    if expected:
        with pytest.raises(ValueError):
            account_Bob.deposit(amount)
    else:
        old_balance = account_Bob.balance
        account_Bob.deposit(amount)
        assert account_Bob.balance == old_balance + amount


# EDGE CASE tesztek

def test_transfer_to_none_account(account_Jhon):
    not_account = "non_account"
    with pytest.raises(TypeError):
        account_Jhon.transfer(10, "non_account")

def test_transfer_to_none_account_negativ(account_Jhon, account_Bob):
   with pytest.raises(ValueError):
    account_Jhon.transfer(-10, account_Jhon)
   

def test_transfer_to_other_account_too_much(account_Jhon, account_Bob):
    with pytest.raises(ValueError):
        account_Jhon.transfer(10000, account_Bob)

# normál müködési tesztek

def test_initial_balance(account_Jhon):
    assert account_Jhon.balance == 50.5

def test_succesfull_transfer(account_Jhon, account_Bob):
    account_Jhon.transfer(25, account_Bob)
    assert account_Jhon.balance == 25.5
    assert account_Bob.balance == 125

    




