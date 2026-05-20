import pytest
from bank_account import BankAccount

@pytest.fixture
def new_bankaccount():
    return BankAccount('Geri')

@pytest.fixture
def existing_bankaccount():
    return BankAccount("Geri",100000)

def test_add_deposit_to_bankaccount(new_bankaccount):
     new_bankaccount.deposit(3)    
     assert new_bankaccount.balance==3

def test_modify_balalnce_to_bankaccount(existing_bankaccount):
     existing_bankaccount.balance=100    
     assert existing_bankaccount.balance==100

def test_get_balance(existing_bankaccount):
    assert existing_bankaccount.get_balance()==100000

def test_change_owner_of_bankaccount(existing_bankaccount):
     existing_bankaccount.owner="Tibi"    
     assert existing_bankaccount.owner=="Tibi"

@pytest.mark.parametrize("owner,expected_exception",[
                            (1,ValueError)#not an str test
                            ])
def test_set_owner_with_excpetions(owner,expected_exception):
     with pytest.raises(expected_exception):
          new_ba=BankAccount(owner)

@pytest.mark.parametrize("owner,balance,expected_exception",[
                            ("Geri",-1,ValueError),#negative test
                            ("Geri","NotValidInput",TypeError)#not a float test  
                            ])
def test_set_balance_with_excpetions(owner,balance,expected_exception):
     with pytest.raises(expected_exception):
          new_ba=BankAccount(owner,balance)

@pytest.mark.parametrize("amount,expected_exception",[
                            (-1,ValueError),#negative test
                            (0,ValueError)#0 test
                           ])
def test_deposit_with_exceptions(existing_bankaccount,amount,expected_exception):
     with pytest.raises(expected_exception):
          existing_bankaccount.deposit(amount)
          
@pytest.mark.parametrize("amount,expected_exception",[
                            (-1,ValueError),#negative test
                            (0,ValueError)#0 test
                           ])
def test_withdraw_with_excpetions(existing_bankaccount,amount,expected_exception):
     with pytest.raises(expected_exception):
          existing_bankaccount.withdraw(amount)
          
@pytest.mark.parametrize("amount,target_account,expected_exception",[
                            (1000,"Jancsi",TypeError),#not a BankAccount instance test
                           ])
def test_transfer_to_not_specific_object_exception(existing_bankaccount,amount,target_account,expected_exception):
     with pytest.raises(expected_exception):
          existing_bankaccount.transfer(amount,target_account)

@pytest.mark.parametrize("amount,target_owner,target_balance,expected_exception",[
                            (1000,"Geri",100000,ValueError),#transfer yourself test
                           ])
def test_transfer_yourself_excpetion(existing_bankaccount,amount,target_owner,target_balance,expected_exception):
     with pytest.raises(expected_exception):
          existing_bankaccount.transfer(amount,BankAccount(target_owner,target_balance))