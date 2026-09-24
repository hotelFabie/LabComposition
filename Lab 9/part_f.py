#Part F

#1
class Account:
    def __init__(self, owner : str, balance : float):
        self.owner = owner
        self.balance = balance

    #2
    def __str__(self):
        return f"Owner: {self.owner}, balance: {self.balance}"

#3
class SavingsAccount(Account):
    def __init__(self, owner : str, balance : float, interest_rate : float):
        super().__init__(owner, balance)

        self.interest_rate = interest_rate

    #4
    def __str__(self):
        return f"Owner: {self.owner}, balance: {self.balance}, interest rate: {self.interest_rate}"

#5
account = Account("Madison Blue", 239999.50)
savings_account = SavingsAccount("Mason Red", 119999.25, 4.5)

print(account)
print(savings_account)