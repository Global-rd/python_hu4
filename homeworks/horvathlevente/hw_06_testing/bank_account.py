from __future__ import annotations
from numbers import Number


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if not isinstance(owner, str):
            raise TypeError("Owner must be a string.")
        if not isinstance(balance, Number):
            raise TypeError("Initial balance must be a number.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = float(balance)
    
    def _validate_amount(self, amount: float):
        if not isinstance(amount, Number):
            raise TypeError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Amount must be positive.")

    def deposit(self, amount: float):
        self._validate_amount(amount)
        self.balance += float(amount)
    
    def withdraw(self, amount: float):
        self._validate_amount(amount)
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= float(amount)

    def transfer(self, amount: float, target_account: "BankAccount"):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if target_account is self:
            raise ValueError("Cannot transfer money to the same account.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
