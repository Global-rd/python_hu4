import pytest
from bank_account import BankAccount


# ============================================================
# FIXTURE-ÖK
# ============================================================

@pytest.fixture
def empty_account():
    """0 egyenlegű új számla."""
    return BankAccount("Marcell", 0.0)


@pytest.fixture
def rich_account():
    """1000 egyenlegű számla."""
    return BankAccount("Anna", 1000.0)


# ============================================================
# ALAP TESZTEK
# ============================================================

def test_account_creation(empty_account):
    assert empty_account.owner == "Marcell"
    assert empty_account.balance == 0.0


def test_deposit_increases_balance(rich_account):
    rich_account.deposit(500)
    assert rich_account.balance == 1500


def test_withdraw_decreases_balance(rich_account):
    rich_account.withdraw(300)
    assert rich_account.balance == 700


# ============================================================
# EXCEPTION TESZTEK
# ============================================================

def test_negative_initial_balance_raises():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount("Test", -100)


def test_withdraw_insufficient_funds_raises(empty_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        empty_account.withdraw(100)


# ============================================================
# PARAMETRIZE
# ============================================================

@pytest.mark.parametrize("invalid_amount", [0, -1, -100, -0.01])
def test_deposit_invalid_amount_raises(rich_account, invalid_amount):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        rich_account.deposit(invalid_amount)


@pytest.mark.parametrize("invalid_amount", [0, -1, -50])
def test_withdraw_invalid_amount_raises(rich_account, invalid_amount):
    with pytest.raises(ValueError, match="Withdraw amount must be positive"):
        rich_account.withdraw(invalid_amount)


# ============================================================
# TRANSFER + EDGE CASE
# ============================================================

def test_transfer_success(rich_account, empty_account):
    rich_account.transfer(200, empty_account)
    assert rich_account.balance == 800
    assert empty_account.balance == 200


@pytest.mark.parametrize("invalid_target", ["string", 123, None, [1, 2, 3]])
def test_transfer_to_non_bankaccount_raises(rich_account, invalid_target):
    with pytest.raises(TypeError, match="Target must be a BankAccount instance"):
        rich_account.transfer(100, invalid_target)


# ============================================================
# EGYÉB
# ============================================================

def test_get_balance(rich_account):
    assert rich_account.get_balance() == 1000.0


def test_str_format(rich_account):
    assert str(rich_account) == "Account owner: Anna, Balance: 1000.00"