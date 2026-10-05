#Part C

#1 and #2
class Printer:
    def __init__(self, model : str, year : int):
        self.model = model
        self.year = year

    def display_status(self) -> None:
        print(f"Model: {self.model}, year: {self.year}")

class Screen:
    def __init__(self, brand : str, second_hand : bool = False):
        self.brand = brand
        self.second_hand = second_hand

    def display_status(self) -> None:
        print(f"Brand: {self.brand}, is second-hand: {self.second_hand}")

#3
devices = [
    Printer("PIXMA TS3751i", 2025),
    Screen("UltraSharp U2424H"),
    Printer("SELPHY CP1000", 2024),
    Screen("Plus S2725HSM", True)
]

#4
for device in devices:
    device.display_status()

#5
#Similarly to how I explained in Part A, duck typing means the greater concern in the language - Python - is about
#the method rather than the class of the object, and this will work because it will find a method with this name in both class types.