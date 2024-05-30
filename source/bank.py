class Transaction:
    def __init__(self) -> None:
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def history_list(self):
        for transaction in self.transactions:
            print(transaction)

class Account(Transaction):
    def __init__(self, account_number: str, balance: int | float = 0) -> None:
        super().__init__()  # Initialize the Transaction class
        self.account_number = str(account_number)
        if balance < 0:
            raise ValueError("Enter the right amount number")
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = value

    def withdraw(self, money: int | float):
        if money > self._balance:
            raise ValueError("Not enough money")
        self._balance -= money
        super().add_transaction(['Withdraw', money])
        return self._balance

    def deposit(self, money: int | float):
        if money < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += money
        super().add_transaction(['Deposit', money])
        return self._balance

class InterestAccount(Account):
    def __init__(self, account_number: str, balance: int | float, interest_rate: int | float) -> None:
        super().__init__(account_number, balance)  # Correct the super call
        self.interest_rate = interest_rate

    def calc_interest(self):
        return self.balance * self.interest_rate

class SavingAccount(InterestAccount):
    def __init__(self, account_number: str, balance: int | float, interest_rate: int | float) -> None:
        super().__init__(account_number, balance, interest_rate)

if __name__ == "__main__":
    acc = SavingAccount(58898765, 1000, 0.14)
    acc.deposit(200)
    acc.withdraw(500)
    acc.deposit(300)
    acc.deposit(700)
    acc.withdraw(500)
    acc.deposit(1200)
    acc.withdraw(900)
    
    acc.history_list()
    print(f"Total Account: {acc._balance}")
