class Character:
    MAX_INVENTORY_SIZE = 3
    
    def __init__(self, name):
        self.name = name

        #Make sure these are private
        self.level = 1
        self.health = 20
        self.defense = 0

        #Does not really have an inventory of sorts yet?:
        # self.inventory = []

        self.exp = 0

        #We'll see if this gets adjusted, or is fixed.
        self.exp_cap = self.level * 10

    #AM I USING THIS???
    def get_level(self) -> int:
        return self.level

    def __str__(self):
        return f"{self.name}"

    def get_profile(self):
        return (f"಄⣀⣠stats of player[{self.name}]⣄⣀಄\n"
        f"•level: {self.level} •health: {self.health} •defense: {self.defense} •current exp: {self.exp}/{self.exp_cap}")

    # def add_to_inventory(self, item : Item):
    #     if len(self.inventory) == self.MAX_INVENTORY_SIZE:
    #         print("inventory is full!")
    #         #NOT SURE ENTIRELY HOW TO BREAK THIS JUST YET...
    #         return
    #     self.inventory.append(item)