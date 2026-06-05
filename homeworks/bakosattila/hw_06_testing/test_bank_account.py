import pytest
from bank_account import BankAccount


# ── Fixtures ─────────────────────

@pytest.fixture
def empty_account():
    return BankAccount("Alice")


@pytest.fixture
def funded_account():
    return BankAccount("Bob", 1000.0)


# ── __init__ ────────────────────

class TestInit:
    def test_default_balance_is_zero(self, empty_account):
        assert empty_account.get_balance() == 0.0

    def test_custom_balance_set_correctly(self, funded_account):
        assert funded_account.get_balance() == 1000.0

    def test_owner_stored_correctly(self, funded_account):
        assert funded_account.owner == "Bob"

    def test_negative_initial_balance_raises(self):
        with pytest.raises(ValueError, match="negative"):
            BankAccount("Eve", -50)

    def test_non_string_owner_raises(self):
        with pytest.raises(TypeError, match="string"):
            BankAccount(123)

    def test_non_numeric_balance_raises(self):
        with pytest.raises(TypeError, match="number"):
            BankAccount("Eve", "hundred")

    def test_bool_balance_raises(self):
        with pytest.raises(TypeError):
            BankAccount("Eve", True)


# ── deposit ────────────────────

class TestDeposit:
    def test_deposit_increases_balance(self, empty_account):
        empty_account.deposit(200)
        assert empty_account.get_balance() == 200.0

    def test_deposit_accumulates(self, funded_account):
        funded_account.deposit(500)
        assert funded_account.get_balance() == 1500.0

    @pytest.mark.parametrize("amount", [0, -1, -100, -0.01])
    def test_deposit_non_positive_raises(self, empty_account, amount):
        with pytest.raises(ValueError, match="positive"):
            empty_account.deposit(amount)

    def test_deposit_string_raises(self, empty_account):
        with pytest.raises(TypeError, match="number"):
            empty_account.deposit("fifty")

    def test_deposit_none_raises(self, empty_account):
        with pytest.raises(TypeError):
            empty_account.deposit(None)

    def test_deposit_bool_raises(self, empty_account):
        with pytest.raises(TypeError):
            empty_account.deposit(True)


# ── withdraw ──────────────────

class TestWithdraw:
    def test_withdraw_decreases_balance(self, funded_account):
        funded_account.withdraw(400)
        assert funded_account.get_balance() == 600.0

    def test_withdraw_exact_balance_empties_account(self, funded_account):
        funded_account.withdraw(1000.0)
        assert funded_account.get_balance() == 0.0

    @pytest.mark.parametrize("amount", [0, -1, -500, -0.01])
    def test_withdraw_non_positive_raises(self, funded_account, amount):
        with pytest.raises(ValueError, match="positive"):
            funded_account.withdraw(amount)

    def test_withdraw_insufficient_funds_raises(self, empty_account):
        with pytest.raises(ValueError, match="Insufficient funds"):
            empty_account.withdraw(1)

    def test_withdraw_more_than_balance_raises(self, funded_account):
        with pytest.raises(ValueError, match="Insufficient funds"):
            funded_account.withdraw(1000.01)

    def test_withdraw_string_raises(self, funded_account):
        with pytest.raises(TypeError, match="number"):
            funded_account.withdraw("ten")

    def test_withdraw_bool_raises(self, funded_account):
        with pytest.raises(TypeError):
            funded_account.withdraw(False)


# ── transfer ─────────

class TestTransfer:
    def test_transfer_decreases_sender_balance(self, funded_account, empty_account):
        funded_account.transfer(300, empty_account)
        assert funded_account.get_balance() == 700.0

    def test_transfer_increases_receiver_balance(self, funded_account, empty_account):
        funded_account.transfer(300, empty_account)
        assert empty_account.get_balance() == 300.0

    def test_transfer_to_non_account_raises(self, funded_account):
        with pytest.raises(TypeError, match="BankAccount"):
            funded_account.transfer(100, "not_an_account")

    def test_transfer_to_dict_raises(self, funded_account):
        with pytest.raises(TypeError):
            funded_account.transfer(100, {"owner": "Hacker"})

    def test_transfer_to_none_raises(self, funded_account):
        with pytest.raises(TypeError):
            funded_account.transfer(100, None)

    def test_transfer_to_self_raises(self, funded_account):
        with pytest.raises(ValueError, match="same account"):
            funded_account.transfer(100, funded_account)

    def test_transfer_insufficient_funds_raises(self, empty_account, funded_account):
        with pytest.raises(ValueError, match="Insufficient funds"):
            empty_account.transfer(1, funded_account)

    def test_transfer_non_numeric_amount_raises(self, funded_account, empty_account):
        with pytest.raises(TypeError, match="number"):
            funded_account.transfer("all", empty_account)

    def test_transfer_zero_amount_raises(self, funded_account, empty_account):
        with pytest.raises(ValueError, match="positive"):
            funded_account.transfer(0, empty_account)

    def test_transfer_negative_amount_raises(self, funded_account, empty_account):
        with pytest.raises(ValueError, match="positive"):
            funded_account.transfer(-50, empty_account)


# ── get_balance ─────────
class TestGetBalance:
    def test_get_balance_returns_correct_value(self, funded_account):
        assert funded_account.get_balance() == 1000.0

    def test_get_balance_after_operations(self, funded_account, empty_account):
        funded_account.deposit(200)
        funded_account.withdraw(100)
        funded_account.transfer(50, empty_account)
        assert funded_account.get_balance() == 1050.0
        assert empty_account.get_balance() == 50.0


# ── __str__ ──────

class TestStr:
    def test_str_format_funded(self, funded_account):
        assert str(funded_account) == "Account owner: Bob, Balance: 1000.00"

    def test_str_format_empty(self, empty_account):
        assert str(empty_account) == "Account owner: Alice, Balance: 0.00"

    def test_str_format_after_deposit(self, empty_account):
        empty_account.deposit(49.5)
        assert str(empty_account) == "Account owner: Alice, Balance: 49.50"
