#Part E

#1
class Product:
    def __init__(self, name : str, price : float):
        self.name = name
        self.price = price

#2
eggs = Product("Eggs", 6.99)

print(eggs)
#Will only print out the object and it's place in memory

#3
class Product:
    def __init__(self, name : str, price : float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product name: {self.name}, price: {self.price}"

#4
tomato = Product("Tomato", 0.79)
bell_pepper =Product ("Bell Pepper", 1.99)
carolina_reaper = Product("Carolina Reaper", 15.99)

print(tomato)
print(bell_pepper)
print(carolina_reaper)

#5
tomato_text = str(tomato)
print(tomato_text)
print(type(tomato_text))
