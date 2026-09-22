#These parts seem to go hand in hand, so...


#Part A
#1
class Book:
    #4
    def __init__(self, title="unknown", author, pages):
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


#4


#5

#Part B
