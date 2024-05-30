import pytest
from oo_projects.source.bank import Account, SavingAccount

@pytest.fixture
def bank() -> Account:
    return Account( 123456, 1000)

@pytest.fixture
def saving_account() -> SavingAccount:
    return SavingAccount(58898765, 1000, 0.14)


def test_withdraw(bank):
    assert bank.withdraw(200) == 800
    
def test_deposit(bank) -> None:
    assert bank.deposit(200) == 1200

def test_negative():
    with pytest.raises(ValueError, match="Enter the right amount number"):
        Account(5248778, -1000)

def test_negative_balance_setter():
    acc = Account("123456", 1000)
    # Trying to set a negative balance should raise a ValueError
    with pytest.raises(ValueError, match="Balance cannot be negative!"):
        acc.balance = -200
    # Verify that the balance remains unchanged after attempting to set an invalid value
    assert acc.balance == 1000  # Assuming initial balance is 1000

def test_interest_rate(saving_account):
    assert saving_account.calc_interest() == 140

@pytest.fixture
def setup_account():
    yield SavingAccount("58898765", 1000, 0.14)



def test_deposit(setup_account):
    acc = setup_account
    acc.deposit(200)
    assert acc.balance == 1200

def test_withdraw(setup_account):
    acc = setup_account
    acc.withdraw(500)
    assert acc.balance == 500

def test_calc_interest(setup_account):
    acc = setup_account
    assert acc.calc_interest() == 1000 * 0.14

def test_history_list(setup_account):
    acc = setup_account
    acc.deposit(200)
    acc.withdraw(500)
    acc.deposit(300)
    
    # Capture print output to test history_list
    import io
    import sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    acc.history_list()
    output = captured_output.getvalue().strip().split('\n')
    
    assert len(output) == 3  # 3 transactions plus the initial balance print
    assert output[0] == "['Deposit', 200]"
    assert output[1] == "['Withdraw', 500]"
    assert output[2] == "['Deposit', 300]"

    sys.stdout = sys.__stdout__  # Reset stdout

if __name__ == "__main__":
    pytest.main()