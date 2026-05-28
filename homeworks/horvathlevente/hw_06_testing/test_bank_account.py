import pytest
from bank_account import BankAccount


# -------- FIXTUREK --------

@pytest.fixture
def account_alice():
    return BankAccount(owner="Alice", balance=100.0)


@pytest.fixture
def account_bob():
    return BankAccount(owner="Bob", balance=50.0)


# -------- ALAP MŰKÖDÉS TESZTEK --------

def test_initial_balance_positive(account_alice):
    assert account_alice.get_balance() == 100.0


def test_deposit_increases_balance(account_alice):
    account_alice.deposit(50)
    assert account_alice.get_balance() == 150.0


def test_withdraw_decreases_balance(account_alice):
    account_alice.withdraw(40)
    assert account_alice.get_balance() == 60.0


def test_transfer_moves_money(account_alice, account_bob):
    account_alice.transfer(30, account_bob)
    assert account_alice.get_balance() == 70.0
    assert account_bob.get_balance() == 80.0


def test_str_representation(account_alice):
    s = str(account_alice)
    assert "Account owner: Alice" in s
    assert "Balance:" in s


# -------- PARAMETRIZE – HIBÁS DEPOSIT INPUTOK --------

@pytest.mark.parametrize("amount", [0, -1, -10.5])
def test_deposit_invalid_amount_raises_value_error(account_alice, amount):
    with pytest.raises(ValueError):
        account_alice.deposit(amount)


@pytest.mark.parametrize("amount", [0, -1, -5])
def test_withdraw_invalid_amount_raises_value_error(account_alice, amount):
    with pytest.raises(ValueError):
        account_alice.withdraw(amount)


# -------- EDGE CASE-EK ÉS EXCEPTION TESZTEK --------

def test_withdraw_insufficient_funds_raises_value_error(account_bob):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account_bob.withdraw(100)


def test_transfer_to_non_bankaccount_raises_type_error(account_alice):
    with pytest.raises(TypeError):
        account_alice.transfer(10, target_account="not-an-account")


def test_initial_negative_balance_raises_value_error():
    with pytest.raises(ValueError):
        BankAccount(owner="Charlie", balance=-10)


def test_initial_non_number_balance_raises_type_error():
    with pytest.raises(TypeError):
        BankAccount(owner="Charlie", balance="not-a-number")


def test_owner_must_be_string():
    with pytest.raises(TypeError):
        BankAccount(owner=123, balance=0)


def test_deposit_non_number_raises_type_error(account_alice):
    with pytest.raises(TypeError):
        account_alice.deposit("not-a-number")


def test_withdraw_non_number_raises_type_error(account_alice):
    with pytest.raises(TypeError):
        account_alice.withdraw("not-a-number")


def test_transfer_non_number_amount_raises_type_error(account_alice, account_bob):
    with pytest.raises(TypeError):
        account_alice.transfer("not-a-number", account_bob)


def test_cannot_transfer_to_self(account_alice):
    with pytest.raises(ValueError, match="Cannot transfer money to the same account"):
        account_alice.transfer(10, account_alice)


# -------- EXTRA: FLOAT ÉS INT KEZELÉS --------

@pytest.mark.parametrize("amount", [10, 10.5])
def test_deposit_accepts_int_and_float(account_bob, amount):
    start = account_bob.get_balance()
    account_bob.deposit(amount)
    assert account_bob.get_balance() == start + float(amount)
