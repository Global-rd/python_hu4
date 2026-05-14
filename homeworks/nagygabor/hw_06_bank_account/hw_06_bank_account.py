"""
hw_06_bank_account.py

"""

from __future__ import annotations
from numbers import Real


# ---------------------------------------------------------------------------
# Egyedi exception-ök
# ---------------------------------------------------------------------------
class BankAccountError(Exception):
    """Általános alap exception minden BankAccount hibára."""


class InvalidAmountError(BankAccountError):
    """Akkor dobódik, ha az összeg nem érvényes (nem szám, vagy <= 0)."""


class InsufficientFundsError(BankAccountError):
    """Akkor dobódik, ha nincs elég pénz a számlán."""


class InvalidAccountError(BankAccountError):
    """Akkor dobódik, ha a címzett nem BankAccount, vagy saját magunk vagyunk."""


# ---------------------------------------------------------------------------
# BankAccount class
# ---------------------------------------------------------------------------
class BankAccount:
    def __init__(self, owner: str, balance: Real = 0):
        # Tulajdonos validálás: string, nem üres
        if not isinstance(owner, str):
            raise TypeError("Owner name must be a string.")
        if not owner.strip():
            raise ValueError("Owner name cannot be empty.")

        # Kezdő egyenleg validálás: szám, nem boolean (mert bool is int Pythonban!),
        # és nem negatív
        if isinstance(balance, bool) or not isinstance(balance, Real):
            raise TypeError("Balance must be a number.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner = owner.strip()
        self.balance = balance

    # -----------------------------------------------------------------------
    # Belső segédfüggvény: összeg validálása
    # -----------------------------------------------------------------------
    @staticmethod
    def _validate_amount(amount) -> None:
        # bool-t kizárjuk, mert Pythonban a True/False is int típus
        if isinstance(amount, bool) or not isinstance(amount, Real):
            raise TypeError(f"Amount must be a number, got {type(amount).__name__}.")
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero.")

    # -----------------------------------------------------------------------
    # Publikus method-ok
    # -----------------------------------------------------------------------
    def deposit(self, amount: Real) -> Real:
        """Pénz befizetése a számlára. Visszaadja az új egyenleget."""
        self._validate_amount(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount: Real) -> Real:
        """Pénz kivétele a számláról. Visszaadja az új egyenleget."""
        self._validate_amount(amount)
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}: balance is only {self.balance}."
            )
        self.balance -= amount
        return self.balance

    def send(self, amount: Real, other: "BankAccount") -> Real:
        """Pénz küldése egy másik BankAccount-nak."""
        if not isinstance(other, BankAccount):
            raise InvalidAccountError(
                "Recipient must be a BankAccount instance."
            )
        if other is self:
            raise InvalidAccountError("Cannot send money to yourself.")

        # Az összeg validálása + elégtelen egyenleg ellenőrzése a withdraw-ban történik
        self.withdraw(amount)
        other.deposit(amount)
        return self.balance

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self.balance})"
