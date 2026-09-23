#Part E

#1
class Device:
    def __init__(self, brand : str, year : int):
        #2
        if year <= 0:
            raise ValueError("Year must be at least 0 or above.")

        self.brand = brand
        self.year = year

        self.is_active = True

#3
class Laptop(Device):
    def __init__(self, brand : str, year : int, ram_gb : int):
        super().__init__(brand, year)

        self.ram_gb = ram_gb

#4
class GamingConsole(Device):
    def __init__(self, brand : str, year : int, name : str):
        super().__init__(brand, year)

        self.name = name

#5
laptop = Laptop("ASUS", 2009, 256)
gamingconsole = GamingConsole("Nintendo", 2025, "Switch 2")


