import pytest
from bank_account import BankAccount

# FIXTURES

@pytest.fixture
def bank_account_empty():
    return BankAccount(owner="Bumm")

@pytest.fixture
def bank_account_rich():
    return BankAccount(owner="Rich", balance=100)


#///////////////
# Static tests
#//////////////

# Test for balance OK
def test_depositing(bank_account_empty) -> None:
    bank_account_empty.deposit(100)
    assert bank_account_empty.get_balance() == 100

# Test for balance NOK
def test_depositing_rich(bank_account_rich) -> None:
    bank_account_rich.deposit(200)
    assert bank_account_rich.get_balance() == 200

# Test for Zero Value
def test_depositing_zero_empty(bank_account_empty) -> None:
    bank_account_empty.deposit(0)
    with pytest.raises(ValueError, match = 'The amount must be positive!'):
        bank_account_empty.deposit(0)

#///////////////
# Parameter tests
#//////////////

# Test for detecting Value errors (PASS)
@pytest.mark.parametrize("amount", [0, -150, -200])
def test_deposit_nok_amounts(bank_account_empty, amount) -> None:
    with pytest.raises(ValueError):
        bank_account_empty.deposit(amount)

# Test for detecting Value errors (FAIL)
@pytest.mark.parametrize("amount", [10, 200])
def test_deposit_ok_amounts(bank_account_rich, amount) -> None:
    with pytest.raises(ValueError):
        bank_account_rich.deposit(amount)

# Transfer error (PASS)
def test_transfer_to_wrong_account(bank_account_rich) -> None:
    invalid_acc = "fals account name"
    with pytest.raises(TypeError):
        bank_account_rich.transfer(invalid_acc, 100)