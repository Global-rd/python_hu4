class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"

account_1 = BankAccount("Haasz", 10000.0)

account_1.deposit(1000.0)

print(account_1)

account_1.withdraw(8000.0)

print("---------------")

print(account_1)

partner_account = BankAccount("Idegen", 5000.0)

account_1.transfer(2000.0, partner_account)

print("----------------------------")
print(account_1)
print(partner_account)

print("----------------------------")

print(account_1.owner)
print(account_1.balance)

print(partner_account.owner)
print(partner_account.balance)