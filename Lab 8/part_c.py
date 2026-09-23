#Part C

#1
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

#2 and #3
class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


#4


#5

