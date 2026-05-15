"""
Bank account model for the testing homework.
"""

from numbers import Real


class BankAccount:
    """Represent a bank account with deposit, withdraw and transfer support."""

    def __init__(self, owner: object, balance: object = 0.0) -> None:
        """Initialize the account with an owner and an optional balance."""
        valid_owner: str = self._validate_owner(owner)
        valid_balance: float = self._validate_number(balance, "Balance")

        if valid_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner: str = valid_owner
        self.balance: float = valid_balance

    def deposit(self, amount: object) -> None:
        """Increase the account balance with a positive amount."""
        valid_amount: float = self._validate_positive_amount(
            amount,
            "Deposit",
        )
        self.balance += valid_amount

    def withdraw(self, amount: object) -> None:
        """Decrease the account balance with a positive amount."""
        valid_amount: float = self._validate_positive_amount(
            amount,
            "Withdraw",
        )

        if valid_amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= valid_amount

    def transfer(self, amount: object, target_account: object) -> None:
        """Transfer a positive amount to another bank account."""
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")

        if target_account is self:
            raise ValueError("Cannot transfer to the same account.")

        valid_amount: float = self._validate_positive_amount(
            amount,
            "Transfer",
        )

        self.withdraw(valid_amount)
        target_account.deposit(valid_amount)

    def get_balance(self) -> float:
        """Return the current account balance."""
        return self.balance

    def _validate_positive_amount(
        self,
        amount: object,
        transaction_type: str,
    ) -> float:
        """Validate that the transaction amount is greater than zero."""
        valid_amount: float = self._validate_number(amount, transaction_type)

        if valid_amount <= 0:
            raise ValueError(f"{transaction_type} amount must be positive.")

        return valid_amount

    def _validate_number(self, value: object, field_name: str) -> float:
        """Validate that the given value is a number and return it as float."""
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError(f"{field_name} must be a number.")

        return float(value)

    def _validate_owner(self, owner: object) -> str:
        """Validate that the account owner is a non-empty string."""
        if not isinstance(owner, str):
            raise TypeError("Owner must be a string.")

        if len(owner.strip()) == 0:
            raise ValueError("Owner cannot be empty.")

        return owner

    def __str__(self) -> str:
        """Return a readable account summary."""
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
