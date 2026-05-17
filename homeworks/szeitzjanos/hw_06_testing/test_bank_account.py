import pytest
from bank_account import BankAccount


# DATAOBJECT FOR TESTING
OWNER_A_NAME = 'PANDACSOKI Boborjan'
OWNER_A_BALANCE = 10000.0

OWNER_B_NAME = 'BESENYO Evettke Zigota'
OWNER_B_BALANCE = 30000.0


# FIXTURES
@pytest.fixture
def owner_a_account() -> BankAccount:
    return BankAccount(OWNER_A_NAME, OWNER_A_BALANCE)

@pytest.fixture
def owner_b_account() -> BankAccount:
    return BankAccount(OWNER_B_NAME, OWNER_B_BALANCE)

# -------------------------------------------------------------------
# TESTS OF DEPOSITES - STEP BY STEP
# -------------------------------------------------------------------
# DEPOSIT POSITIVE TESTS
def test_positive_deposit_by_owner_a(owner_a_account) -> None:
    owner_a_account.deposit(2000)
    assert owner_a_account.balance == 12000

def test_positive_deposit_by_owner_b(owner_b_account) -> None:
    owner_b_account.deposit(5000)
    assert owner_b_account.balance == 35000

# DEPOSIT NEGATIVE TESTS
def test_zero_value_of_deposit(owner_a_account) -> None:
    with pytest.raises(
        ValueError, match = 'The amount must be positive!'
    ):
        owner_a_account.deposit(0)

def test_negative_value_of_deposit(owner_a_account) -> None:
    with pytest.raises(
        ValueError, match = 'The amount must be positive!'
    ):
        owner_a_account.deposit(-5000)

def test_not_number_value_of_deposit(owner_a_account) -> None:
    with pytest.raises(
        ValueError, match = 'Only numeric values are allowed!'
    ):
        owner_a_account.deposit('Horse')

def test_none_value_of_deposit(owner_a_account) -> None:
    with pytest.raises(
        TypeError, match = 'Only numeric values are allowed!'
    ):
        owner_a_account.deposit(None)

# -------------------------------------------------------------------
# TESTS OF DEPOSITES - BATCH CHECKING
# -------------------------------------------------------------------
GOOD_VALUES_D = [0.0000000000000000001, 1000, 5000, 10000]
WRONG_VALUES_D = [0,                    # zero is not acceptable
                  -0.1, -1, -5000,      # negatives are not acceptable
                  'Horse',              # only digits allowed
                  None]                 # only digits allowed

@pytest.mark.parametrize('amount', GOOD_VALUES_D)
def test_some_good_value_of_deposit(owner_a_account, amount) -> None:
    owner_a_account.deposit(amount)

@pytest.mark.parametrize('amount', WRONG_VALUES_D)
def test_any_wrong_value_of_deposit(owner_a_account, amount) -> None:
    with pytest.raises(
        (ValueError, TypeError),match =
                        'The amount must be positive!|'
                        'Only numeric values are allowed!|'
                        'Only numeric values are allowed!'
    ):
        owner_a_account.deposit(amount)

# -------------------------------------------------------------------
# TESTS OF WITHDRAW - STEP BY STEP
# -------------------------------------------------------------------
# WITHDRAW POSITIVE TESTS
def test_positive_withdraw_by_owner_a(owner_a_account) -> None:
    owner_a_account.withdraw(2000)
    assert owner_a_account.balance == 8000

def test_positive_withdraw_by_owner_b(owner_b_account) -> None:
    owner_b_account.withdraw(5000)
    assert owner_b_account.balance == 25000

# WITHDRAW NEGATIVE TESTS
def test_zero_value_of_withdraw(owner_a_account) -> None:
    with pytest.raises(
        ValueError, match = 'The amount must be positive!'
    ):
        owner_a_account.withdraw(0)

def test_negative_value_of_withdraw(owner_a_account) -> None:
    with pytest.raises(
        ValueError, match = 'The amount must be positive!'
    ):
        owner_a_account.withdraw(-5000)

def test_bigger_then_possible_value_of_withdraw(owner_a_account) -> None:
    with pytest.raises(
        ValueError, match = 'Insufficient funds!'
    ):
        owner_a_account.withdraw(11000)

def test_not_number_value_of_withdraw(owner_a_account) -> None:
    with pytest.raises(
        ValueError, match = 'Only numeric values are allowed!'
    ):
        owner_a_account.withdraw('Horse')

def test_none_value_of_withdraw(owner_a_account) -> None:
    with pytest.raises(
        TypeError, match = 'Only numeric values are allowed!'
    ):
        owner_a_account.withdraw(None)

# -------------------------------------------------------------------
# TESTS OF WITHDRAW - BATCH CHECKING
# -------------------------------------------------------------------
GOOD_VALUES_W = [0.0000000000000000001, 1000, 5000, 10000]
WRONG_VALUES_W = [0,                       # zero is not acceptable
                  -0.000000001, -1, -5000, # negatives are not acceptable
                  10001, 20000,            # account has insufficient balance
                  'Horse',                 # only digits allowed
                  None]                    # only digits allowed

@pytest.mark.parametrize('amount', GOOD_VALUES_W)
def test_some_good_value_of_withdraw(owner_a_account, amount) -> None:
    owner_a_account.withdraw(amount)

@pytest.mark.parametrize('amount', WRONG_VALUES_W)
def test_any_wrong_value_of_deposit(owner_a_account, amount) -> None:
    with pytest.raises(
        (ValueError, TypeError),
        match = 'The amount must be positive!|'
        'Insufficient funds!|'
        'Only numeric values are allowed!|'
        'Only numeric values are allowed!'
    ):
        owner_a_account.withdraw(amount)

# -------------------------------------------------------------------
# TESTS OF TRANSFER - STEP BY STEP
# -------------------------------------------------------------------
# TRANSFER POSITIVE TESTS
def test_positive_transfer_by_owner_a(owner_a_account, owner_b_account) -> None:
    owner_a_account.transfer(2000, owner_b_account)
    assert owner_a_account.balance == 8000
    assert owner_b_account.balance == 32000

def test_positive_transfer_by_owner_b(owner_b_account, owner_a_account) -> None:
    owner_b_account.transfer(5000, owner_a_account)
    assert owner_a_account.balance == 15000
    assert owner_b_account.balance == 25000

# TRANSFER NEGATIVE TESTS
def test_zero_value_of_transfer(owner_a_account, owner_b_account) -> None:
    with pytest.raises(
        ValueError, match = 'The amount must be positive!'
    ):
        owner_a_account.transfer(0, owner_b_account)

def test_negative_value_of_transfer(owner_a_account, owner_b_account) -> None:
    with pytest.raises(
        ValueError, match = 'The amount must be positive!'
    ):
        owner_a_account.transfer(-5000, owner_b_account)

def test_bigger_then_possible_value_of_transfer(owner_a_account, owner_b_account) -> None:
    with pytest.raises(
        ValueError, match = 'Insufficient funds!'
    ):
        owner_a_account.transfer(11000, owner_b_account)

def test_not_number_value_of_transfer(owner_a_account, owner_b_account) -> None:
    with pytest.raises(
        ValueError, match = 'Only numeric values are allowed!'
    ):
        owner_a_account.transfer('Horse', owner_b_account)

def test_none_value_of_transfer(owner_a_account, owner_b_account) -> None:
    with pytest.raises(
        TypeError, match = 'Only numeric values are allowed!'
    ):
        owner_a_account.transfer(None, owner_b_account)

# -------------------------------------------------------------------
# TESTS OF TRANSFER - BATCH CHECKING
# -------------------------------------------------------------------
GOOD_VALUES_T = [0.0000000000000000001, 1000, 5000, 10000]
WRONG_VALUES_T = [0,                       # zero is not acceptable
                  -0.000000001, -1, -5000, # negatives are not acceptable
                  10001, 20000,            # account has insufficient balance
                  'Horse',                 # only digits allowed
                  None]                    # only digits allowed

@pytest.mark.parametrize('amount', GOOD_VALUES_T)
def test_some_good_value_of_transfer(owner_a_account, owner_b_account, amount) -> None:
    owner_a_account.transfer(amount, owner_b_account)

@pytest.mark.parametrize('amount', WRONG_VALUES_T)
def test_any_wrong_value_of_transfer(owner_a_account, owner_b_account, amount) -> None:
    with pytest.raises(
        (ValueError, TypeError),
        match = 'The amount must be positive!|'
                'Insufficient funds!|'
                'Only numeric values are allowed!|'
                'Only numeric values are allowed!'
    ):
        owner_a_account.transfer(amount, owner_b_account)

# -------------------------------------------------------------------
# TEST OF EXTRA TRANSFER FEATURE
# -------------------------------------------------------------------
# TRANSFER NEGATIVE TEST
def test_transfer_to_own_account(owner_a_account) -> None:
    with pytest.raises(
        TypeError, match = 'Target must be a BankAccount instance!'
    ):
        owner_a_account.transfer(10000, object)
