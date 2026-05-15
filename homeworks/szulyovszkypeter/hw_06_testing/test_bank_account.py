'''
Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a tesztjeidben használsz.
● Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak érdekében, hogy a tesztet több input-ra is lefuttassa
  (pl: teszteld a deposit() method-ot pontosan 0 és negatív szám inputtal is).
● Tesztelj edge case-eket (pl: pénz küldése nem BankAccount object-nek).
● Írj teszteket amik arra irányulnak, hogy a megfelelő Exception raise-elődik- e a megadott input-ra.
'''

import pytest
from bank_account import BankAccount

# --- FIXTURES ---

@pytest.fixture
def empty_account():
    """Létrehoz egy alapértelmezett, 0 egyenlegű számlát."""
    return BankAccount(owner="TesztSima", balance=0.0)

@pytest.fixture
def funded_account():
    """Létrehoz egy 1000 egységgel feltöltött számlát."""
    return BankAccount(owner="TesztMany", balance=1000.0)

# --- TESZTEK ---

def test_initial_balance_fail():
    """Teszteli, hogy negatív egyenleggel nem lehet számlát nyitni."""
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("Szulyo", balance=-50.0)

@pytest.mark.parametrize("deposit_amount", [0, -10, -0.01])
def test_deposit_invalid_amounts(empty_account, deposit_amount):
    """Paraméterezett teszt: a deposit() csak pozitív számot fogadhat el."""
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        empty_account.deposit(deposit_amount)

def test_withdraw_success(funded_account):
    """Teszteli a sikeres kifizetést."""
    funded_account.withdraw(500)
    assert funded_account.get_balance() == 500.0

def test_withdraw_insufficient_funds(funded_account):
    """Teszteli a fedezethiány miatti hibát (Edge case)."""
    with pytest.raises(ValueError, match="Insufficient funds."):
        funded_account.withdraw(1001.0)

def test_transfer_success(funded_account, empty_account):
    """Teszteli a sikeres utalást két számla között."""
    funded_account.transfer(400, empty_account)
    assert funded_account.get_balance() == 600.0
    assert empty_account.get_balance() == 400.0

def test_transfer_to_invalid_object(funded_account):
    """Edge case: Pénz küldése nem BankAccount típusú objektumnak."""
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        funded_account.transfer(100, "NemEgySzámlaObjektum")

def test_str_representation(funded_account):
    """Teszteli a __str__ metódus formátumát."""
    assert str(funded_account) == "Account owner: TesztMany, Balance: 1000.00"

# Új tesztek
def test_transfer_to_self(funded_account):
    """Teszteli, hogy nem lehet pénzt átutalni saját számlára."""
    with pytest.raises(ValueError, match="Cannot transfer money to the same account."):
        funded_account.transfer(100, funded_account)

@pytest.fixture
def acc_tesztszaz():
    return BankAccount("TesztSzáz", 100.0)

@pytest.fixture
def acc_tesztotven():
    return BankAccount("TesztÖtven", 50.0)

@pytest.mark.parametrize("invalid_input", ["100", None, [], {}, "pénz"])
def test_invalid_type_inputs(acc_tesztszaz, invalid_input):
    """Ellenőrzi, hogy a metódusok dobják-e a TypeError-t nem szám típusú bemenetnél."""
    with pytest.raises(TypeError):
        acc_tesztszaz.deposit(invalid_input)
    with pytest.raises(TypeError):
        acc_tesztszaz.withdraw(invalid_input)

@pytest.mark.parametrize("invalid_owner", [123, "", "   ", None])
def test_invalid_owner_name(invalid_owner):
    """Ellenőrzi, hogy ne lehessen üres vagy nem string nevű tulajdonos."""
    with pytest.raises(ValueError, match="Owner name must be a non-empty string."):
        BankAccount(owner=invalid_owner)

def test_initial_balance_type_check():
    """A konstruktor is ellenőrizze az egyenleg típusát."""
    with pytest.raises(TypeError):
        BankAccount("Nemjó", balance="sok")

def test_transfer_integration(acc_tesztszaz, acc_tesztotven):
    """Sikeres utalás integrációs tesztje."""
    acc_tesztszaz.transfer(30, acc_tesztotven)
    assert acc_tesztszaz.get_balance() == 70.0
    assert acc_tesztotven.get_balance() == 80.0


