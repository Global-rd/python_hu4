import pytest
from bank_account import BankAccount


# ---------------------------------------------------------------------------
# FIXTURE-ök
# ---------------------------------------------------------------------------

@pytest.fixture
def basic_account():
    """Egyszerű számla 500 induló egyenleggel – általános tesztekhez."""
    return BankAccount("Kovács Barnabás", 500.0)

@pytest.fixture
def empty_account():
    """Nulla egyenlegű számla – fedezethiány és edge case tesztekhez."""
    return BankAccount("Teszt Elek", 0.0)


# ---------------------------------------------------------------------------
# __init__ tesztek
# ---------------------------------------------------------------------------

class TestInit:
    def test_valid_creation(self, basic_account):
        """Helyes adatokkal létrejön a számla."""
        assert basic_account.owner == "Kovács Barnabás"
        assert basic_account.balance == 500.0

    def test_default_balance_is_zero(self):
        """Ha nem adunk meg egyenleget, 0 az alapértelmezett."""
        acc = BankAccount("Valaki")
        assert acc.get_balance() == 0.0

    def test_negative_initial_balance_raises(self):
        """Negatív induló egyenleg ValueError-t dob."""
        with pytest.raises(ValueError, match="cannot be negative"):
            BankAccount("Valaki", -100)

    # EXTRA: non-number balance
    def test_non_number_balance_raises(self):
        """String egyenleg TypeError-t dob."""
        with pytest.raises(TypeError, match="must be a number"):
            BankAccount("Valaki", "ezer forint")

    # EXTRA: üres / nem-string owner
    def test_empty_owner_raises(self):
        """Üres string owner TypeError-t dob."""
        with pytest.raises(TypeError, match="non-empty string"):
            BankAccount("", 100)

    def test_non_string_owner_raises(self):
        """Szám típusú owner TypeError-t dob."""
        with pytest.raises(TypeError, match="non-empty string"):
            BankAccount(123, 100)


# ---------------------------------------------------------------------------
# deposit() tesztek
# ---------------------------------------------------------------------------

class TestDeposit:
    def test_deposit_increases_balance(self, basic_account):
        """Érvényes befizetés növeli az egyenleget."""
        basic_account.deposit(200)
        assert basic_account.get_balance() == 700.0

    # Parametrize: 0 és negatív értékek mind ValueError-t kell dobjanak
    @pytest.mark.parametrize("amount", [0, -1, -100, -0.01])
    def test_deposit_non_positive_raises(self, basic_account, amount):
        """0 és negatív befizetés ValueError-t dob."""
        with pytest.raises(ValueError, match="must be positive"):
            basic_account.deposit(amount)

    # EXTRA: non-number input
    @pytest.mark.parametrize("bad_input", ["száz", None, [100], True, False])
    def test_deposit_non_number_raises(self, basic_account, bad_input):
        """Nem szám típusú input (bool is beleértve) TypeError-t dob."""
        with pytest.raises(TypeError, match="must be a number"):
            basic_account.deposit(bad_input)


# ---------------------------------------------------------------------------
# withdraw() tesztek
# ---------------------------------------------------------------------------

class TestWithdraw:
    def test_withdraw_decreases_balance(self, basic_account):
        """Érvényes kivét csökkenti az egyenleget."""
        basic_account.withdraw(100)
        assert basic_account.get_balance() == 400.0

    def test_withdraw_exact_balance(self, basic_account):
        """Pontosan az egyenleg összegét ki lehet venni."""
        basic_account.withdraw(500)
        assert basic_account.get_balance() == 0.0

    def test_withdraw_insufficient_funds_raises(self, empty_account):
        """Fedezethiány esetén ValueError-t dob."""
        with pytest.raises(ValueError, match="Insufficient funds"):
            empty_account.withdraw(1)

    @pytest.mark.parametrize("amount", [0, -50, -0.01])
    def test_withdraw_non_positive_raises(self, basic_account, amount):
        """0 és negatív kivét ValueError-t dob."""
        with pytest.raises(ValueError, match="must be positive"):
            basic_account.withdraw(amount)

    # EXTRA: non-number input
    def test_withdraw_non_number_raises(self, basic_account):
        """Nem szám típusú input TypeError-t dob."""
        with pytest.raises(TypeError, match="must be a number"):
            basic_account.withdraw("kétszáz")


# ---------------------------------------------------------------------------
# transfer() tesztek
# ---------------------------------------------------------------------------

class TestTransfer:
    def test_transfer_moves_money(self, basic_account, empty_account):
        """Utalás után a küldő egyenlege csökken, a fogadóé nő."""
        basic_account.transfer(200, empty_account)
        assert basic_account.get_balance() == 300.0
        assert empty_account.get_balance() == 200.0

    def test_transfer_to_non_bankaccount_raises(self, basic_account):
        """Nem BankAccount célra utalás TypeError-t dob."""
        with pytest.raises(TypeError, match="Target must be a BankAccount"):
            basic_account.transfer(100, "nem_szamla")

    def test_transfer_to_dict_raises(self, basic_account):
        """Dict típusú célra utalás TypeError-t dob (edge case)."""
        with pytest.raises(TypeError):
            basic_account.transfer(100, {"owner": "hacker"})

    def test_transfer_insufficient_funds_raises(self, empty_account, basic_account):
        """Fedezethiány esetén transfer is ValueError-t dob."""
        with pytest.raises(ValueError, match="Insufficient funds"):
            empty_account.transfer(1, basic_account)

    def test_transfer_full_balance(self, basic_account, empty_account):
        """Az összes pénzt át lehet utalni."""
        basic_account.transfer(500, empty_account)
        assert basic_account.get_balance() == 0.0
        assert empty_account.get_balance() == 500.0

    # EXTRA: saját magunknak való utalás
    def test_transfer_to_self_raises(self, basic_account):
        """Saját számlára való utalás ValueError-t dob."""
        with pytest.raises(ValueError, match="same account"):
            basic_account.transfer(100, basic_account)


# ---------------------------------------------------------------------------
# get_balance() és __str__() tesztek
# ---------------------------------------------------------------------------

class TestMisc:
    def test_get_balance_returns_correct_value(self, basic_account):
        """get_balance() pontosan az aktuális egyenleget adja vissza."""
        assert basic_account.get_balance() == 500.0

    def test_str_representation(self, basic_account):
        """__str__ helyes formátumú stringet ad vissza."""
        result = str(basic_account)
        assert "Kovács Barnabás" in result
        assert "500.00" in result