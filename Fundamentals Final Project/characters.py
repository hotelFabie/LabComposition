#IMPORTANT: Give every method important comments.

import enemies

class Character:
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.health = 20
        self.defense = 0 + (self.level / 2) 
        self.temporary_defense = 0

        self.exp = 0
        self.exp_cap = 10

        self.kills = {"normal" : 0, "weird" : 0, "great" : 0}

    def __str__(self):
        return f"{self.name}"

    #OBS: Can't this be an __str__?
    def get_profile(self):
        return (f"಄⣀⣠stats of player: [{self.name}]⣄⣀಄\n"
        f"•level: {self.level} •health: {self.health} •defense: {self.defense} •current exp: {self.exp}/{self.exp_cap}")

    def choose_action(self, enemy : enemies.Enemy):
        print("•[a] attack •[d] defend")
        action = input(">")

        while (action != "a") and (action != "d"):
            print("choose a or d!")
            action = input(">")

        if action == "a":
            enemy.health -= 5
            print(f"you attacked the enemy with 5 damage! ٩(ˋᗣˊ*)و")

            if enemy.health <= 0:
                #Not fully decided yet, just making sure it works first.
                #Why does it interpret it as a "literal"?
                exp = int(3)
                print(f"enemy defeated! gained {exp} exp.⋆⭒˚｡⋆")
                
                self.add_exp(exp)
        elif action == "d":
            print(f"you defended with 1 defense, and healed 5 hp! ☥")
            self.health += 5
            self.temporary_defense += 1
            print(f"DEBUG: temporary defense is {self.temporary_defense}")
            

    def add_exp(self, exp : float):
        if (self.exp + exp >= self.exp_cap):
            self.level += 1
            print(f"leveled up! {self.level - 1} → {self.level}")

            self.exp = (self.exp + exp) % self.exp_cap 
            self.exp_cap = 10 * (self.level * 0.75)
        else:
            self.exp += exp