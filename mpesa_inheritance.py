class Account:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully. New balance is {self.balance}")
        else:
            print("Amount should be greater than zero")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount should be greater than zero")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully. New balance is {self.balance}")

    def __str__(self):
        return f"Account holder: {self.account_holder}\nBalance: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest added successfully. New balance is {self.balance:.2f}")

    def __str__(self):
        return (f"Savings account holder: {self.account_holder}\n"
                f"Balance: {self.balance:.2f}\n"
                f"Interest rate: {self.interest_rate}%")


# Example usage:
account = Account(account_holder='john', balance=1000)
account.deposit(-100)  # Outputs: Amount should be greater than zero
account.withdraw(500)  # Outputs: 500 withdrawn successfully. New balance is 500
print(account)

savings = SavingsAccount(account_holder='jane', balance=500, interest_rate=14)
savings.deposit(500)  # Outputs: 500 deposited successfully. New balance is 1000
savings.withdraw(500)  # Outputs: 500 withdrawn successfully. New balance is 500
savings.add_interest()  # Outputs: Interest added successfully. New balance is 570.00
print(savings)
