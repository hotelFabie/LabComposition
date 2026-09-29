#IMPORTANT: Type hinting.

import enemies

class Character:
    MAX_LEVEL = 10 
    
    DAMAGE_BASE = 5
    EXP_BASE = 10
    HEALTH_BASE = 20

    #The following constants are made in relation to...
    DAMAGE_INCREASE = 0.5
    DEFENSE_INCREASE = 0.5
    EXP_CAP_MULTIPLIER = 0.75
    EXP_WALK_INCREASE = 0.25
    HEALTH_FACTOR = 2
    HEALTH_INCREASE = 5
    
    
    def __init__(self, name):
        self.name = name
        self.level = 1

        self.damage = self.DAMAGE_BASE

        self.defense = 0
        self.temporary_defense = 0

        self.health = self.HEALTH_BASE
        self.health_cap = self.HEALTH_BASE

        self.exp = 0
        self.exp_cap = self.EXP_BASE

        self.steps = 0
        self.kills = {"normal enemy" : 0, "weird enemy" : 0, "great enemy" : 0}

    def __str__(self):
        return f"{self.name}"

    def get_status(self) -> str:
        """
        Gives a status overview of the player's character data and progress.
        """

        status = f"಄⣀⣠stats of player: [{self.name}]⣄⣀಄\n" 
        exp_str = f"{self.exp}/{self.exp_cap}"

        if self.level >= self.MAX_LEVEL: 
            exp_str = f"MAX"

        kills_str = ", ".join(f"{enemy}: {amount}" for enemy, amount in self.kills.items()) 
        
        status += f"•level: {self.level} •health: {self.health}/{self.health_cap} •damage: {self.damage} •defense: {self.defense} •current exp: {exp_str}\n•kills: [{kills_str}]\n•steps taken: {self.steps}"
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

        if action == "a":
            enemy.health -= self.damage
            print(f"you attacked the enemy with {self.damage} damage! ٩(ˋᗣˊ*)و")

            if enemy.health <= 0:
                exp = enemy.difficulty.value
                self.add_exp(exp)
                
                print(f"enemy defeated! gained {exp} exp.⋆⭒˚｡⋆")
                
        elif action == "d":
            #Might need it to be HEALTH.
            if self.health + self.HEALTH_INCREASE > self.health_cap:
                self.health = self.health_cap
            else:
                self.health += self.HEALTH_INCREASE
            self.temporary_defense += 1
            print(f"you defended with {self.temporary_defense} defense, and healed {self.HEALTH_INCREASE} hp! ☥")

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

                #INCREASE THE DAMAGE AS WELL.
                #Maybe that we break this out, so it becomes a bit less crowded.
                self.exp_cap = self.EXP_BASE * (self.level * self.EXP_CAP_MULTIPLIER)
                #Remaining magic number.
                self.health_cap = self.HEALTH_BASE + (self.level / self.HEALTH_FACTOR)
                self.health = self.health_cap
                self.damage += self.DAMAGE_INCREASE
            else:
                self.exp += exp