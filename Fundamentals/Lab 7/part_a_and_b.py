#These parts seem to go hand in hand, so...


#Part A
#1
class Book:
    #4
    def __init__(self, author, pages, title="<unknown>"):
        self.title = title
        self.author = author
        self.pages = pages

    #1 (Part B)
    def is_long(self) -> bool:
        if self.pages > 300:
            return True
        return False


#2
class Laptop:
    def __init__(self, brand, model, ram_gb, price):
        self.brand = brand
        self.model = model
        self.ram_gb = ram_gb
        self.price = price

#3
book1 = Book("Hell", "The Devil", 1000)
book2 = Book("Hell", "The Devil", 1000)
print(book1 is book2)

#5
kw_book = Book(author="Joe Xi", pages=390, title="Chinese History")

#Part B
#2
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    #3
    def withdrawal(self, amount):
        new_balance = self.balance - amount
        if new_balance < 0:
            raise ValueError("Attempted withdrawal failed, due to requested amount being higher")
        self.balance = new_balance

#4
class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False

#5
task1 = Task("Jumping Jacks", True)
task2 = Task("Clean living room", True)

#Proof
task1.reopen()
print(task1.completed)
print(task2.completed)
#Task 1 will have False, and Task 2 will have True.
#They are instance attributes, and so they belong to the object itself.