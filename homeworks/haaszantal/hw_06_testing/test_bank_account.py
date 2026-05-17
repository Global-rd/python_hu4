import pytest
from bank_account import BankAccount

@pytest.fixture
def base_account():
    return BankAccount("Alice", 6000.0)

@pytest.fixture
def partner_base_account():
    return BankAccount("Tom", 5000.0)

#teszt deposit
def test_deposit_changed_balance(base_account):
    base_account.deposit(1000.0)
    assert base_account.balance == 7000

#teszt withdraw
def test_withdraw_changed_balance(base_account):
    base_account.withdraw(1000)
    assert base_account.balance == 5000

#teszt base_account és partner_base_account balance ellenőrzés 
def test_transfer_partner_changed_balance(base_account, partner_base_account):
    base_account.transfer(5000, partner_base_account)
    assert partner_base_account.balance == 10000
    assert base_account.balance == 1000

@pytest.mark.parametrize("amount, expected_exception", [
    (0, ValueError),
    (-1000, ValueError),
])

#parametrize teszt    
def test_deposit_invalid_amount (base_account, amount, expected_exception):
    with pytest.raises(expected_exception):
         base_account.deposit(amount)

#Edge case
def test_transfer_partner_account_not_bankaccount_type_error(base_account):
    with pytest.raises(TypeError):
         base_account.transfer(1000, "no BankAccount")

#error tesztek

#error_deposit_exception_rase
def test_deposit_value_error(base_account):
    with pytest.raises(ValueError):
        base_account.deposit(-1000)

#error_withdraw_excepton_rase_negative_amount
def test_withdraw_value_error_1(base_account):
    with pytest.raises(ValueError):
        base_account.withdraw(-2000)

#error_withdraw_excepton_rase_amount_bigger_than_balance
def test_withdraw_value_error_1(base_account):
    with pytest.raises(ValueError):
        base_account.withdraw(7000)

#error_base_account_negative_balance
def test_create_negative_balance():
    with pytest.raises(ValueError):
        base_account = BankAccount("Jimmy", -2000)
