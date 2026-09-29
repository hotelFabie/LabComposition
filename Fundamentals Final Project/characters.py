#IMPORTANT: Give every method important comments.

import enemies

class Character:
    MAX_LEVEL = 15
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.defense = 0 + (self.level / 2) 
        self.temporary_defense = 0

        self.health = 20.0
        self.health_cap = 20.0

        self.exp = 0
        self.exp_cap = 10

        self.steps = 0

        self.kills = {"normal enemy" : 0, "weird enemy" : 0, "great enemy" : 0}

    def __str__(self):
        return f"{self.name}"

    #OBS: Can't this be an __str__?
    #Also, it might not write it out directly as I would think immediately.
    def get_status(self):
        status = f"಄⣀⣠stats of player: [{self.name}]⣄⣀಄\n" 
        exp_str = f"{self.exp}/{self.exp_cap}"

        if self.level >= self.MAX_LEVEL: 
            exp_str = f"MAX"

        #Needed to search this up.
        kills_str = ", ".join(f"{enemy}: {amount}" for enemy, amount in self.kills.items()) 
        
        status += f"•level: {self.level} •health: {self.health}/{self.health_cap} •defense: {self.defense} •current exp: {exp_str}\n•kills: [{kills_str}]\n•steps taken: {self.steps}"
        return status

    def choose_action(self, enemy : enemies.Enemy):
        print("\n•[a] attack •[d] defend")
        action = input(">")

        while (action != "a") and (action != "d"):
            print("\nchoose a or d!")
            action = input(">")

        if action == "a":
            enemy.health -= 5
            print(f"you attacked the enemy with 5 damage! ٩(ˋᗣˊ*)و")

            if enemy.health <= 0:
                #Not fully decided yet, just making sure it works first.
                #Why does it interpret it as a "literal"?
                exp = enemy.difficulty.value + 1
                print(f"enemy defeated! gained {exp} exp.⋆⭒˚｡⋆")
                
                self.add_exp(exp)
        elif action == "d":
            print(f"you defended with 1 defense, and healed 5 hp! ☥")
            if self.health + 5 > self.health_cap:
                self.health = self.health_cap
            else:
                self.health += 5
            self.temporary_defense += 1

    def add_exp(self, exp : float):
        #A check for if it reaches beyond the MAX LEVEL or not.
        if not self.level < self.MAX_LEVEL:
            print("already max level, so no exp is gained.")
        else:
            if (self.exp + exp >= self.exp_cap):
                self.level += 1
                print(f"leveled up! {self.level - 1} → {self.level}")

                self.exp = (self.exp + exp) % self.exp_cap 
                self.exp_cap = 10 * (self.level * 0.75)
                self.health_cap = 20 + (self.level / 2)
                self.health = self.health_cap
            else:
                self.exp += exp