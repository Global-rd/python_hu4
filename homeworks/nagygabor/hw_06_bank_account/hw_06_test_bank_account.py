"""
hw_06_test_bank_account.py

Pytest tesztek a BankAccount class-hez.

Futtatás:
    pytest -v hw_06_test_bank_account.py
"""

import pytest

from hw_06_bank_account import (
    BankAccount,
    InvalidAmountError,
    InsufficientFundsError,
    InvalidAccountError,
)


# ===========================================================================
# FIXTURE-ÖK (legalább 2 különböző BankAccount object)
# ===========================================================================
@pytest.fixture
def empty_account():
    """Egy újonnan nyitott, 0 egyenlegű számla."""
    return BankAccount("Alice", 0)


@pytest.fixture
def rich_account():
    """Egy számla 1000-es kezdő egyenleggel."""
    return BankAccount("Bob", 1000)


@pytest.fixture
def two_accounts():
    """Két különböző számla, utaláshoz használjuk."""
    sender = BankAccount("Sender", 500)
    receiver = BankAccount("Receiver", 100)
    return sender, receiver


# ===========================================================================
# __init__ tesztek
# ===========================================================================
class TestInit:
    def test_create_account_with_defaults(self):
        acc = BankAccount("Charlie")
        assert acc.owner == "Charlie"
        assert acc.balance == 0

    def test_create_account_with_balance(self, rich_account):
        assert rich_account.owner == "Bob"
        assert rich_account.balance == 1000

    def test_owner_name_is_stripped(self):
        acc = BankAccount("  Dave  ", 50)
        assert acc.owner == "Dave"

    @pytest.mark.parametrize("invalid_owner", [123, None, [], {}, 12.5])
    def test_non_string_owner_raises(self, invalid_owner):
        with pytest.raises(TypeError):
            BankAccount(invalid_owner, 100)

    @pytest.mark.parametrize("empty_owner", ["", "   ", "\t\n"])
    def test_empty_owner_raises(self, empty_owner):
        with pytest.raises(ValueError):
            BankAccount(empty_owner, 100)

    def test_negative_initial_balance_raises(self):
        with pytest.raises(ValueError):
            BankAccount("Eve", -10)

    @pytest.mark.parametrize("bad_balance", ["100", None, [50], True, False])
    def test_non_number_balance_raises(self, bad_balance):
        with pytest.raises(TypeError):
            BankAccount("Frank", bad_balance)


# ===========================================================================
# deposit() tesztek — parametrize-zal több inputra
# ===========================================================================
class TestDeposit:
    @pytest.mark.parametrize(
        "amount, expected_balance",
        [
            (100, 100),
            (0.01, 0.01),
            (1_000_000, 1_000_000),
            (50.75, 50.75),
        ],
    )
    def test_deposit_valid_amounts(self, empty_account, amount, expected_balance):
        empty_account.deposit(amount)
        assert empty_account.balance == expected_balance

    def test_deposit_returns_new_balance(self, rich_account):
        new_balance = rich_account.deposit(500)
        assert new_balance == 1500
        assert rich_account.balance == 1500

    def test_multiple_deposits(self, empty_account):
        empty_account.deposit(100)
        empty_account.deposit(50)
        empty_account.deposit(25)
        assert empty_account.balance == 175

    @pytest.mark.parametrize("invalid_amount", [0, -1, -100, -0.5])
    def test_deposit_zero_or_negative_raises(self, empty_account, invalid_amount):
        with pytest.raises(InvalidAmountError):
            empty_account.deposit(invalid_amount)

    @pytest.mark.parametrize(
        "invalid_amount",
        ["100", None, [100], {"amount": 100}, True, False],
    )
    def test_deposit_non_number_raises(self, empty_account, invalid_amount):
        with pytest.raises(TypeError):
            empty_account.deposit(invalid_amount)

    def test_failed_deposit_does_not_change_balance(self, rich_account):
        original = rich_account.balance
        with pytest.raises(InvalidAmountError):
            rich_account.deposit(-50)
        assert rich_account.balance == original


# ===========================================================================
# withdraw() tesztek
# ===========================================================================
class TestWithdraw:
    @pytest.mark.parametrize(
        "amount, expected_balance",
        [
            (1, 999),
            (500, 500),
            (1000, 0),
            (0.5, 999.5),
        ],
    )
    def test_withdraw_valid_amounts(self, rich_account, amount, expected_balance):
        rich_account.withdraw(amount)
        assert rich_account.balance == expected_balance

    def test_withdraw_returns_new_balance(self, rich_account):
        new_balance = rich_account.withdraw(200)
        assert new_balance == 800

    def test_withdraw_more_than_balance_raises(self, rich_account):
        with pytest.raises(InsufficientFundsError):
            rich_account.withdraw(1500)

    def test_withdraw_from_empty_account_raises(self, empty_account):
        with pytest.raises(InsufficientFundsError):
            empty_account.withdraw(1)

    @pytest.mark.parametrize("invalid_amount", [0, -1, -100])
    def test_withdraw_zero_or_negative_raises(self, rich_account, invalid_amount):
        with pytest.raises(InvalidAmountError):
            rich_account.withdraw(invalid_amount)

    @pytest.mark.parametrize("invalid_amount", ["100", None, [50], True])
    def test_withdraw_non_number_raises(self, rich_account, invalid_amount):
        with pytest.raises(TypeError):
            rich_account.withdraw(invalid_amount)

    def test_failed_withdraw_does_not_change_balance(self, rich_account):
        original = rich_account.balance
        with pytest.raises(InsufficientFundsError):
            rich_account.withdraw(99999)
        assert rich_account.balance == original


# ===========================================================================
# send() tesztek — edge case-ek és exception tesztek
# ===========================================================================
class TestSend:
    def test_send_transfers_money(self, two_accounts):
        sender, receiver = two_accounts
        sender.send(200, receiver)
        assert sender.balance == 300
        assert receiver.balance == 300

    def test_send_returns_sender_new_balance(self, two_accounts):
        sender, receiver = two_accounts
        result = sender.send(100, receiver)
        assert result == 400

    # --- Edge case-ek ---
    @pytest.mark.parametrize(
        "not_an_account",
        ["Alice", 12345, None, [], {"owner": "X"}, object()],
    )
    def test_send_to_non_bankaccount_raises(self, rich_account, not_an_account):
        """Edge case: pénz küldése nem BankAccount object-nek."""
        with pytest.raises(InvalidAccountError):
            rich_account.send(100, not_an_account)

    def test_send_to_self_raises(self, rich_account):
        """Edge case: saját magunknak nem küldhetünk pénzt."""
        with pytest.raises(InvalidAccountError):
            rich_account.send(100, rich_account)

    def test_send_insufficient_funds_raises(self, two_accounts):
        sender, receiver = two_accounts
        with pytest.raises(InsufficientFundsError):
            sender.send(9999, receiver)

    def test_failed_send_does_not_change_either_balance(self, two_accounts):
        """Ha az utalás elbukik, egyik egyenleg sem változhat."""
        sender, receiver = two_accounts
        sender_balance = sender.balance
        receiver_balance = receiver.balance

        with pytest.raises(InsufficientFundsError):
            sender.send(9999, receiver)

        assert sender.balance == sender_balance
        assert receiver.balance == receiver_balance

    @pytest.mark.parametrize("invalid_amount", [0, -50, "100", None])
    def test_send_invalid_amount_raises(self, two_accounts, invalid_amount):
        sender, receiver = two_accounts
        with pytest.raises((InvalidAmountError, TypeError)):
            sender.send(invalid_amount, receiver)

    def test_send_invalid_amount_does_not_change_balances(self, two_accounts):
        sender, receiver = two_accounts
        s_before, r_before = sender.balance, receiver.balance
        with pytest.raises(InvalidAmountError):
            sender.send(-10, receiver)
        assert sender.balance == s_before
        assert receiver.balance == r_before


# ===========================================================================
# Integrációs / kombinált tesztek
# ===========================================================================
class TestCombinedScenarios:
    def test_deposit_then_withdraw(self, empty_account):
        empty_account.deposit(500)
        empty_account.withdraw(200)
        assert empty_account.balance == 300

    def test_chain_of_transfers(self):
        a = BankAccount("A", 1000)
        b = BankAccount("B", 0)
        c = BankAccount("C", 0)

        a.send(500, b)
        b.send(200, c)

        assert a.balance == 500
        assert b.balance == 300
        assert c.balance == 200

    def test_total_money_preserved_after_transfer(self, two_accounts):
        """A rendszerben lévő összes pénz utalás után is ugyanannyi."""
        sender, receiver = two_accounts
        total_before = sender.balance + receiver.balance
        sender.send(150, receiver)
        total_after = sender.balance + receiver.balance
        assert total_before == total_after
