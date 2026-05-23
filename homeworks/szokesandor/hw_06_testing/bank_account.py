class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self._check_number_type(balance, "balance")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance

    # Non-number esetén exception-t generál
    def _check_number_type(self, number: any, field_name: str):
        if type(number) not in (int, float):
            raise TypeError(f"The {field_name} must be a number.")
    
    def deposit(self, amount: float):
        self._check_number_type(amount, "amount") # Exception-t generál, ha az amount paraméter nem szám
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        self._check_number_type(amount, "withdraw amount") # Exception-t generál, ha az amount paraméter nem szám
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        self._check_number_type(amount, "amount") # Exception-t generál, ha az amount paraméter nem szám
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if target_account is self: # Ha a cél számla megegyezik a saját számlával, akkor exception generálódik. Saját magunknak nem utalhatunk!
            raise ValueError("The target account cannot be the same as the initiating account.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
