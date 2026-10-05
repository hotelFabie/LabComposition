#Part C

#1
class Product:
    #2
    tax_rate = 15

    def __init__(self, name, price):
        self.name = name
        self.price = price

    #3
    def price_with_tax(self) -> float:
        return self.price * (1 + self.tax_rate / 100)
     
#4
p1 = Product("Juggling Balls", 150)
p2 = Product("Metronome", 400)
p3 = Product("Telekinetic Transmitter", 1100)

print(f"Product 1's price with tax: {p1.price_with_tax()}")
print(f"Product 2's price with tax: {p2.price_with_tax()}")
print(f"Product 3's price with tax: {p3.price_with_tax()}")

#5
Product.tax_rate = 17.5

print(f"Product 1's price w. updated tax: {p1.price_with_tax()}")
print(f"Product 2's price w. updated tax: {p2.price_with_tax()}")
print(f"Product 3's price w. updated tax: {p3.price_with_tax()}")
#The effect is that this method, which utilizes the tax_rate, will produce a slightly higher result.

#6
p1.tax_rate = 20
print(p1.tax_rate) 
print(p2.tax_rate)
print(Product.tax_rate)

#Gives (in order, from top to bottom): 20, 17.5 and 17.5
