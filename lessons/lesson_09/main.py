from bank_account import BankAccount, InsufficientFundsError, InvalidAmountError


def main():
    account_1 = BankAccount(account_holder="X",
                            account_number="1",
                            balance=500.0)
    
    account_1.deposit(100.0)
    print(account_1.get_balance())
    print(account_1._balance)
    account_1.withdraw(300.0)
    print(account_1._transactions)
    print(account_1.get_transaction_history())

if __name__ == "__main__":
    main()



