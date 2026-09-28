class Character:
    def __init__(self, name):
        self.name = name

        #exp cap of sorts.

        self.level = 1
        self.health = 20
        self.defense = 0
        self.exp = 0

    def get_level(self) -> int:
        return self.level

    #Will probably need a singleton pattern, because we either have one, or nothing.
