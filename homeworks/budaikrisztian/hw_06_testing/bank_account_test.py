"""
Homework 6: Bank account tests.
Author: Budai Krisztian
"""

import pytest
from lib.bank_account import BankAccount

# Shared fixture data for reusable test accounts.
SOURCE_OWNER = "Source Owner"
SOURCE_INITIAL_BALANCE = 1000.0
TARGET_OWNER = "Target Owner"
TARGET_INITIAL_BALANCE = 200.0

# Shared invalid amount cases for positive amount validation.
ZERO_OR_NEGATIVE_AMOUNTS = [
    pytest.param(0.0, id="zero"),
    pytest.param(-50.0, id="negative"),
]

# Owner values that are strings but should still be rejected.
EMPTY_OWNER_VALUES = [
    pytest.param("", id="empty-string"),
    pytest.param("   ", id="spaces-only"),
]

# Values used when a string input is required.
NON_STRING_VALUES = [
    pytest.param(123, id="integer"),
    pytest.param(None, id="none"),
    pytest.param(True, id="boolean"),
    pytest.param([], id="list"),
    pytest.param({}, id="dict"),
    pytest.param(object(), id="object"),
    pytest.param((), id="tuple"),
]

# Values used when a numeric input is required.
NON_NUMBER_VALUES = [
    pytest.param("100", id="string"),
    pytest.param(None, id="none"),
    pytest.param(True, id="boolean"),
    pytest.param([], id="list"),
    pytest.param({}, id="dict"),
    pytest.param(object(), id="object"),
    pytest.param((), id="tuple"),
]

# Values used when a BankAccount transfer target is required.
NON_BANK_ACCOUNT_TARGETS = [
    pytest.param(TARGET_OWNER, id="string"),
    pytest.param(None, id="none"),
    pytest.param([], id="list"),
    pytest.param({}, id="dict"),
    pytest.param(object(), id="object"),
    pytest.param((), id="tuple"),
]


@pytest.fixture
def source_account() -> BankAccount:
    """Create a bank account with an initial balance."""
    return BankAccount(SOURCE_OWNER, SOURCE_INITIAL_BALANCE)


@pytest.fixture
def target_account() -> BankAccount:
    """Create a second bank account for transfer tests."""
    return BankAccount(TARGET_OWNER, TARGET_INITIAL_BALANCE)


class TestBankAccountInitialization:
    """Tests for creating BankAccount objects."""

    def test_uses_default_balance(self) -> None:
        """The default balance should be zero."""
        # Arrange + Act
        account = BankAccount("Default Owner")

        # Assert
        assert account.owner == "Default Owner", "Checks the saved owner name."
        assert account.get_balance() == 0.0, "Checks the default balance."

    def test_stores_initial_balance(self) -> None:
        """The constructor should store a valid initial balance."""
        # Arrange + Act
        account = BankAccount("Initial Owner", 500.0)

        # Assert
        assert account.get_balance() == 500.0, "Checks the initial balance."

    @pytest.mark.parametrize(
        "owner",
        EMPTY_OWNER_VALUES,
    )
    def test_rejects_empty_owner(
        self,
        owner: str,
    ) -> None:
        """Empty owner names should not be accepted."""
        # Arrange comes from the parametrized owner input.

        # Act + Assert
        with pytest.raises(ValueError, match="Owner cannot be empty."):
            BankAccount(owner)

    @pytest.mark.parametrize(
        "owner",
        NON_STRING_VALUES,
    )
    def test_rejects_non_string_owner(
        self,
        owner: object,
    ) -> None:
        """Owner must be a string."""
        # Arrange comes from the parametrized owner input.

        # Act + Assert
        with pytest.raises(TypeError, match="Owner must be a string."):
            BankAccount(owner)

    def test_rejects_negative_balance(
        self,
    ) -> None:
        """Initial balance cannot be negative."""
        # Arrange
        owner = "Negative Owner"
        balance = -1.0

        # Act + Assert
        with pytest.raises(
            ValueError,
            match="Initial balance cannot be negative.",
        ):
            BankAccount(owner, balance)

    @pytest.mark.parametrize(
        "balance",
        NON_NUMBER_VALUES,
    )
    def test_rejects_non_number_balance(
        self,
        balance: object,
    ) -> None:
        """Initial balance must be a number."""
        # Arrange comes from the parametrized balance input.

        # Act + Assert
        with pytest.raises(TypeError, match="Balance must be a number."):
            BankAccount("Invalid Balance Owner", balance)


class TestDeposit:
    """Tests for depositing money."""

    def test_increases_balance(
        self,
        source_account: BankAccount,
    ) -> None:
        """Deposit should add the amount to the current balance."""
        # Arrange
        deposit_amount = 250.0

        # Act
        source_account.deposit(deposit_amount)

        # Assert
        assert source_account.get_balance() == (
            SOURCE_INITIAL_BALANCE + deposit_amount
        ), "Checks that deposit increases the balance."

    @pytest.mark.parametrize(
        "amount",
        ZERO_OR_NEGATIVE_AMOUNTS,
    )
    def test_rejects_zero_or_negative_amount(
        self,
        source_account: BankAccount,
        amount: float,
    ) -> None:
        """Deposit should reject zero and negative amounts."""
        # Arrange comes from the parametrized amount input.

        # Act + Assert
        with pytest.raises(
            ValueError,
            match="Deposit amount must be positive.",
        ):
            source_account.deposit(amount)

    @pytest.mark.parametrize(
        "amount",
        NON_NUMBER_VALUES,
    )
    def test_rejects_non_number_amount(
        self,
        source_account: BankAccount,
        amount: object,
    ) -> None:
        """Deposit should reject values that are not valid numbers."""
        # Arrange comes from the parametrized amount input.

        # Act + Assert
        with pytest.raises(TypeError, match="Deposit must be a number."):
            source_account.deposit(amount)


class TestWithdraw:
    """Tests for withdrawing money."""

    def test_decreases_balance(
        self,
        source_account: BankAccount,
    ) -> None:
        """Withdraw should subtract the amount from the current balance."""
        # Arrange
        withdraw_amount = 400.0

        # Act
        source_account.withdraw(withdraw_amount)

        # Assert
        assert source_account.get_balance() == (
            SOURCE_INITIAL_BALANCE - withdraw_amount
        ), "Checks that withdraw decreases the balance."

    @pytest.mark.parametrize(
        "amount",
        ZERO_OR_NEGATIVE_AMOUNTS,
    )
    def test_rejects_zero_or_negative_amount(
        self,
        source_account: BankAccount,
        amount: float,
    ) -> None:
        """Withdraw should reject zero and negative amounts."""
        # Arrange comes from the parametrized amount input.

        # Act + Assert
        with pytest.raises(
            ValueError,
            match="Withdraw amount must be positive.",
        ):
            source_account.withdraw(amount)

    def test_rejects_amount_greater_than_balance(
        self,
        source_account: BankAccount,
    ) -> None:
        """Withdraw should fail when the account has insufficient funds."""
        # Arrange
        withdraw_amount = SOURCE_INITIAL_BALANCE + 1.0

        # Act + Assert
        with pytest.raises(ValueError, match="Insufficient funds."):
            source_account.withdraw(withdraw_amount)

    @pytest.mark.parametrize(
        "amount",
        NON_NUMBER_VALUES,
    )
    def test_rejects_non_number_amount(
        self,
        source_account: BankAccount,
        amount: object,
    ) -> None:
        """Withdraw should reject values that are not valid numbers."""
        # Arrange comes from the parametrized amount input.

        # Act + Assert
        with pytest.raises(TypeError, match="Withdraw must be a number."):
            source_account.withdraw(amount)


class TestTransfer:
    """Tests for transferring money between accounts."""

    def test_moves_money_between_accounts(
        self,
        source_account: BankAccount,
        target_account: BankAccount,
    ) -> None:
        """Transfer should withdraw from source and deposit to target."""
        # Arrange
        transfer_amount = 300.0

        # Act
        source_account.transfer(transfer_amount, target_account)

        # Assert
        assert source_account.get_balance() == (
            SOURCE_INITIAL_BALANCE - transfer_amount
        ), "Checks that transfer decreases the source balance."
        assert target_account.get_balance() == (
            TARGET_INITIAL_BALANCE + transfer_amount
        ), "Checks that transfer increases the target balance."

    def test_rejects_same_account(
        self,
        source_account: BankAccount,
    ) -> None:
        """Transfer should reject sending money to the same account."""
        # Arrange
        transfer_amount = 100.0

        # Act + Assert
        with pytest.raises(
            ValueError,
            match="Cannot transfer to the same account.",
        ):
            source_account.transfer(transfer_amount, source_account)

    @pytest.mark.parametrize(
        "target_account",
        NON_BANK_ACCOUNT_TARGETS,
    )
    def test_rejects_non_bank_account_target(
        self,
        source_account: BankAccount,
        target_account: object,
    ) -> None:
        """Transfer target must be another BankAccount object."""
        # Arrange comes from the parametrized target account input.

        # Act + Assert
        with pytest.raises(
            TypeError,
            match="Target must be a BankAccount instance.",
        ):
            source_account.transfer(100.0, target_account)

    @pytest.mark.parametrize(
        "amount",
        ZERO_OR_NEGATIVE_AMOUNTS,
    )
    def test_rejects_zero_or_negative_amount_and_keeps_balances_unchanged(
        self,
        source_account: BankAccount,
        target_account: BankAccount,
        amount: float,
    ) -> None:
        """Failed transfer should not change either account balance."""
        # Arrange comes from the parametrized amount input.

        # Act + Assert
        with pytest.raises(
            ValueError,
            match="Transfer amount must be positive.",
        ):
            source_account.transfer(amount, target_account)

        # Assert
        assert source_account.get_balance() == SOURCE_INITIAL_BALANCE, (
            "Checks that failed transfer leaves source balance unchanged."
        )
        assert target_account.get_balance() == TARGET_INITIAL_BALANCE, (
            "Checks that failed transfer leaves target balance unchanged."
        )

    @pytest.mark.parametrize(
        "amount",
        NON_NUMBER_VALUES,
    )
    def test_rejects_non_number_amount(
        self,
        source_account: BankAccount,
        target_account: BankAccount,
        amount: object,
    ) -> None:
        """Transfer should reject values that are not valid numbers."""
        # Arrange comes from the parametrized amount input.

        # Act + Assert
        with pytest.raises(TypeError, match="Transfer must be a number."):
            source_account.transfer(amount, target_account)

        # Assert
        assert source_account.get_balance() == SOURCE_INITIAL_BALANCE, (
            "Checks that failed transfer leaves source balance unchanged."
        )
        assert target_account.get_balance() == TARGET_INITIAL_BALANCE, (
            "Checks that failed transfer leaves target balance unchanged."
        )


class TestStringRepresentation:
    """Tests for readable account formatting."""

    def test_returns_readable_account_summary(
        self,
        source_account: BankAccount,
    ) -> None:
        """The string representation should include owner and balance."""
        # Arrange
        expected_text = (
            f"Account owner: {source_account.owner}, "
            f"Balance: {source_account.balance:.2f}"
        )

        # Act
        actual_text = str(source_account)

        # Assert
        assert actual_text == expected_text, (
            "Checks the account string format."
        )
