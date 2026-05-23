import pytest
from bank_account import BankAccount


# Fixture -ök létrehozása 

@pytest.fixture
def bank_account_empty():
    return BankAccount(owner="Penniless Pete")

@pytest.fixture
def bank_account_anita():
    return BankAccount(owner="Anita Bug", balance=1000)

@pytest.fixture
def bank_account_richie():
    return BankAccount(owner="Richie Rich", balance=5000000)


# Depositing, withdrawing, transfering és get_balance tesztelése a fenti fixture -ök használatával. Megvizsgáljuk, hogy a műveletek végrehajtása után a számlaegyenleg az elvártaknak megfelelően alakul-e.

def test_depositing(bank_account_empty):
    bank_account_empty.deposit(100)
    assert bank_account_empty.get_balance() == 100

def test_withdrawing(bank_account_richie):
    original_balance = bank_account_richie.get_balance()
    withdraw_amount = 1000
    bank_account_richie.withdraw(withdraw_amount)
    assert bank_account_richie.get_balance() == original_balance - withdraw_amount

def test_transfering(bank_account_richie, bank_account_anita):
    original_balance_richie = bank_account_richie.get_balance()
    original_balance_anita = bank_account_anita.get_balance()
    transfer_amount = 1000
    bank_account_richie.transfer(transfer_amount, bank_account_anita)
    assert bank_account_richie.get_balance() == original_balance_richie - transfer_amount  # Richie számlája lecsökkent
    assert bank_account_anita.get_balance() == original_balance_anita + transfer_amount    # Anita számlája meghízott


# Többször előforduló regexp-es kifejezések exception-ban elvárt üzenetek ellenőrzéséhez

mustbe_positive = r"^.+must be positive.$"
mustbe_number = r"^.+must be a number.$"


# Deposit method tesztelése @pytest.mark.parametrize használatával. A tesz során azt vizsgáljuk, hogy generálódik-e a megfelelő exception, ha az amount értéke nulla, negatív vagy nem szám.

@pytest.mark.parametrize("amount, expected_exception,  message_text_end", [
    (-100, ValueError, mustbe_positive),    # Negatív amount
    (0, ValueError, mustbe_positive),       # Nulla amount
    ("cicamica", TypeError, mustbe_number)  # Ha az amount nem szám
])
def test_depositing_with_invalid_input(bank_account_anita, amount, expected_exception,  message_text_end):
    with pytest.raises(expected_exception, match=message_text_end):
        bank_account_anita.deposit(amount)


# Withdraw method tesztelése, amelynek során azt vizsgáljuk, hogy generálódik-e a megfelelő exception, ha az amount értéke nulla, negatív vagy nem szám, vagy ha nincs elegendő egyenleg.

@pytest.mark.parametrize("amount, expected_exception,  message_text_end", [
    (-100, ValueError, mustbe_positive),          # Negatív amount
    (0, ValueError, mustbe_positive),             # Nulla amount
    ("bodrikutya", TypeError, mustbe_number),     # Ha az amount nem szám
    (2000, ValueError, r"^Insufficient funds.$")  # Ha nincs elegendő zsé a számlán
])
def test_withdrawing_with_invalid_input(bank_account_anita, amount, expected_exception,  message_text_end):
    with pytest.raises(expected_exception, match=message_text_end):
        bank_account_anita.withdraw(amount)


# Pénz küldése nem BankAccount object-nek.

def test_transfer_2_nobank_account(bank_account_anita):
    with pytest.raises(TypeError, match=r"^Target must be a BankAccount instance.$"):
        bank_account_anita.transfer(100, "OTP Bank Account")


# Pénz küldése saját bankszámlára.

def test_transfer_2_self_account(bank_account_anita):
    with pytest.raises(ValueError, match=r"^The target account cannot be the same as the initiating account.$"):
        bank_account_anita.transfer(100, bank_account_anita)


# Teszteljük a megfelelő string megjelenítést.

def test_object_2_str(bank_account_anita):
    assert bank_account_anita.__str__() == "Account owner: Anita Bug, Balance: 1000.00"
