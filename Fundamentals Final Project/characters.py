import enemies

class Character:
    #MAX_INVENTORY_SIZE = 3
    
    def __init__(self, name):
        self.name = name

        #Make sure these are private
        self.level = 1
        self.health = 20
        self.defense = 0

        self.exp = 0

        #We'll see if this gets adjusted, or is fixed.
        self.exp_cap = self.level * 10

    def __str__(self):
        return f"{self.name}"

    def get_profile(self):
        return (f"಄⣀⣠stats of player[{self.name}]⣄⣀಄\n"
        f"•level: {self.level} •health: {self.health} •defense: {self.defense} •current exp: {self.exp}/{self.exp_cap}")

    def choose_action(self, enemy : enemies.Enemy):
        print("•[a] attack •[d] defend")
        action = input(">")

        while (action != "a") and (action != "d"):
            print("choose a or d!")
            action = input(">")

        if action == "a":
            enemy.health -= 5
            if enemy.health <= 0:
                #Not fully decided yet, just making sure it works first.
                #Why does it interpret it as a "literal"?
                exp = int(3)
                print(f"enemy defeated! {exp}")
                self.add_exp(exp)
        elif action == "d":
            pass

    def add_exp(self, exp : int):

        #May not work as intended immediately, might have to change some of the logic.
        if (self.exp + exp >= self.exp_cap):
            self.level += 1
            self.exp = 0 + self.exp_cap % self.exp 
            self.exp_cap = 10 * self.level
        else:
            self.exp += exp
