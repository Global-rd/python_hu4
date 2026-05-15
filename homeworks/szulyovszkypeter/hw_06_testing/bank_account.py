"""
Extra: 
Típusellenőrzés: Bevezettem egy segédmetódust (_validate_number), amely ellenőrzi, hogy az összeg int vagy float típusú-e. 
Ezt minden tranzakciónál meghívjuk.
Önhivatkozás tiltása: A transfer metódus most már ellenőrzi, hogy a target_account nem azonos-e a forrásszámlával.
Owner validáció: Biztosítjuk, hogy a tulajdonos neve ne legyen üres vagy érvénytelen típus.
Ezekre plusz tesztek íródtak.
"""

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        '''Ellenőrzés. hogy nem lehet negatív egyenleggel számlát nyitni, és hogy a tulajdonos neve érvényes string legyen, 
           valamint helyes formátumú a kezdőegyenleg.
        '''
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner name must be a non-empty string.")
        self._validate_number(balance, "Initial balance")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    def _validate_number(self, value, field_name):
        """Segéd a numerikus bemenetek ellenőrzésére."""
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field_name} must be a number.")

    def deposit(self, amount: float):
        '''Pénz befizetése a számlára. Az összegnek pozitívnak kell lennie.'''
        self._validate_number(amount, "Deposit amount")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        '''Pénz felvétele a számláról. Az összegnek pozitívnak kell lennie. Nem lehet több, mint a jelenlegi egyenleg.'''
        self._validate_number(amount, "Withdraw amount")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        '''Pénz átutalása egy másik BankAccount objektumra. Az összegnek pozitívnak kell lennie, és nem lehet több, mint a jelenlegi egyenleg.'''
        self._validate_number(amount, "Transfer amount")
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if target_account is self:
            raise ValueError("Cannot transfer money to the same account.")
        
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        '''Visszaadja a számla aktuális egyenlegét.'''
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
    