class BankAccount:
    '''
    *** DEFINITION OF A BANK ACCOUNT CLASS AND ITS METHOD DESCRIPTIONS ***
    '''

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        '''
        *** VALIDATION OF THE OWNER'S NAME ***
        '''
        if owner.strip() == '':
            raise ValueError(
                'The owner\'s name is required and cannot be empty!'
            )
        if not all(char.lower().isalpha() or char == ' ' or char == "." for char in owner.strip()):
            raise TypeError(
                'Invalid characters detected in the owner\'s name!'
                )

        '''
        *** VALIDATION OF THE OWNER'S BALANCE ***
        '''
        if balance < 0:
            raise ValueError(
                'Initial balance cannot be negative!'
            )

        '''
        *** CLASS DESCRIPTION ***
        '''
        self.owner = owner
        self.balance = balance


    def is_amount_positive(self, amount:float) -> bool:
        if amount == None:
            raise TypeError(
                'Only numeric values are allowed!'
            )

        try:
            amount = float(amount)
        except ValueError:
            raise ValueError(
                'Only numeric values are allowed!'
            )

        if amount <= 0:
            raise ValueError(
                'The amount must be positive!'
            )
        return True


    def deposit(self, amount: float) -> None:
        '''
        *** INCREMENTS THE BALANCE BY THE GIVEN AMOUNT ***
        '''
        if self.is_amount_positive(amount):
            self.balance += float(amount)


    def withdraw(self, amount: float) -> None:
        '''
        *** VALIDATION OF THE BALANCE AND THE AMOUNT TO BE WITHDRAWN ***
        '''
        if self.is_amount_positive(amount) and float(amount) > self.balance:
            raise ValueError(
                'Insufficient funds!'
            )

        '''
        *** PROCESSING THE WITHDRAWAL BY REDUCING THE ACCOUNT BALANCE ***
        '''
        if self.is_amount_positive(amount):
            self.balance -= float(amount)


    def transfer(self, amount: float, target_account: "BankAccount") -> None:
        '''
        *** VERIFICATION OF THE EXISTENCE OF THE SPECIFIED BANK IDENTIFIER ***
        '''
        if not isinstance(target_account, BankAccount):
            raise TypeError(
                'Target must be a BankAccount instance!'
            )

        '''
        *** VERIFICATION OF PROHIBITED BANK TRANSFERS ***
        '''
        if target_account is self:
            raise TypeError(
                'The target of the transfer cannot be the same account!'
            )

        '''
        *** PROCESSING THE BANK TRANSACTION ***
        '''
        if self.is_amount_positive(amount):
            self.withdraw(float(amount))
            target_account.deposit(float(amount))


    def get_balance(self) -> float:
        '''
        *** RETURNS A VALUE FOR THE BALANCE ***
        '''
        return self.balance


    def __str__(self) -> str:
        '''
        *** RETURNS DETAILS ABOUT THE OWNER AND THEIR ACCOUNT BALANCE ***
        '''
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
