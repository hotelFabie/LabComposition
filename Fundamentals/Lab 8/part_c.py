#Part C

#1
class Account:
    def __init__(self, owner : str, balance : float):
        self.owner = owner
        self.balance = balance

#2 and #3
class SavingsAccount(Account):
    def __init__(self, owner : str, balance : float, interest_rate : float):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate


#4
sa1 = SavingsAccount("James", 500, 4.5)
sa2 = SavingsAccount("Annica", 800, 3.5)
print(f"Acc. 1: {sa1.owner}, balance: {sa1.balance}, interest rate: {sa1.interest_rate}")
print(f"Acc. 1: {sa2.owner}, balance: {sa2.balance}, interest rate: {sa2.interest_rate}")

#5
#SavingsAccount is an Account because a savings account is a type of account. 
