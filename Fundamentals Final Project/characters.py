class Character:
    def __init__(self, name):
        self.name = name


        self.level = 1
        self.health = 20
        self.defense = 0
        self.exp = 0

    def get_level(self) -> int:
        return self.level

    #Just testing
    def __str__(self):
        return f"[{self.name}]"


#Exp cap of sorts.

#Will probably need a singleton pattern, because we either have one, or nothing.
