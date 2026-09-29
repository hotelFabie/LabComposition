#IMPORTANT: Give every method important comments.

import enemies

class Character:
    MAX_LEVEL = 15
    EXP_BASE = 10
    HEALTH_BASE = 20
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.defense = 0 + (self.level / 2) 
        self.temporary_defense = 0

        self.health = self.HEALTH_BASE
        self.health_cap = self.HEALTH_BASE

        self.exp = 0
        self.exp_cap = self.EXP_BASE

        self.steps = 0

        self.kills = {"normal enemy" : 0, "weird enemy" : 0, "great enemy" : 0}

    def __str__(self):
        return f"{self.name}"

    #Highly unlikely that we every would need an __str__, unless you want to see this as it. 
    #Felt the naming to be more understandable.
    def get_status(self) -> str:
        """
        Gives a status overview of the player's character data and progress.
        """

        status = f"಄⣀⣠stats of player: [{self.name}]⣄⣀಄\n" 
        exp_str = f"{self.exp}/{self.exp_cap}"

        if self.level >= self.MAX_LEVEL: 
            exp_str = f"MAX"

        #Needed to search this up.
        kills_str = ", ".join(f"{enemy}: {amount}" for enemy, amount in self.kills.items()) 
        
        status += f"•level: {self.level} •health: {self.health}/{self.health_cap} •defense: {self.defense} •current exp: {exp_str}\n•kills: [{kills_str}]\n•steps taken: {self.steps}"
        return status

    def choose_action(self, enemy : enemies.Enemy) -> None:
        """
        Gives user action choices while in battle.
        Allowed actions are attacking and defending.
        Attacking: Causes damage against enemy.
        Defending: Heightens defense and heals. 
        """

        print("\n•[a] attack •[d] defend")
        action = input(">")

        while (action != "a") and (action != "d"):
            print("\nchoose a or d!")
            action = input(">")

        #This may be a little hardcoded, as we do not have any set damage for the character.
        if action == "a":
            enemy.health -= 5
            print(f"you attacked the enemy with 5 damage! ٩(ˋᗣˊ*)و")

            if enemy.health <= 0:
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
        """
        Adds experience points to the character only if they are below the max level.
        Updates the level if experience cap is reached, while increasing both the experience and health cap, plus restoring health.
        """
        if not self.level < self.MAX_LEVEL:
            print("already max level, so no exp is gained.")
        else:
            if (self.exp + exp >= self.exp_cap):
                self.level += 1
                print(f"leveled up! {self.level - 1} → {self.level}")

                self.exp = (self.exp + exp) % self.exp_cap 

                self.exp_cap = self.EXP_BASE * (self.level * 0.75)
                self.health_cap = self.HEALTH_BASE + (self.level / 2)
                self.health = self.health_cap
            else:
                self.exp += exp