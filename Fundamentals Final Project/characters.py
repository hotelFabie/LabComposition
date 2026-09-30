#IMPORTANT: Type hinting.

import enemies

class Character:
    MAX_LEVEL = 10 
    DAMAGE_BASE = 5
    EXP_BASE = 10
    HEALTH_BASE = 50
    HEAL = 5

    #One universal factor for increasing status values when levelling up.
    STATUS_FACTOR = 0.5

    def __init__(self, name):
        """
        Constructor method for the character.
        Get initialized with start values that can gradually go up if user levels up through game progression.
        """
        self.name = name
        self.level = 1

        self.inventory = []

        self.damage = self.DAMAGE_BASE

        self.main_def = 0
        self.temp_def = 0

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
        #Start of the string we'll add onto before we return.
        status = f"಄⣀⣠stats of player: [{self.name}]⣄⣀಄\n" 
        
        #Experience formatted.
        exp_str = f"{self.exp}/{self.exp_cap}"
        if self.level >= self.MAX_LEVEL: 
            exp_str = f"MAX"

        #Kills formatted.
        kills_str = ", ".join(f"{enemy}: {amount}" for enemy, amount in self.kills.items()) 
        
        status += (f"•level: {self.level} •health: {self.health}/{self.health_cap} "
            f"•damage: {self.damage} •defense: {self.main_def} "
            f"•current exp: {exp_str}\n•kills: [{kills_str}]\n•steps taken: {self.steps}")

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
                self.health += self.HEAL
                self.add_exp(exp)
                
                print(f"enemy defeated! gained {exp} exp.⋆⭒˚｡⋆")
                
        elif action == "d":
            if self.health + self.HEAL > self.health_cap:
                self.health = self.health_cap
            else:
                self.health += self.HEAL
            self.temp_def += self.STATUS_FACTOR
            print(f"you defended with {self.temp_def} defense, and healed {self.HEAL} hp! ☥")

    def add_exp(self, exp : float):
        """
        Adds experience points to the character only if they are below the max level.
        Updates the level if experience cap is reached, while increasing both the experience and health cap, plus restoring health.
        """
        if not self.level < self.MAX_LEVEL:
            print("already max level, so no exp is gained.")
        else:
            if (self.exp + exp >= self.exp_cap):
                #In the case where you level up, stats get increased and health gets restored.
                self.level += 1
                print(f"leveled up! {self.level - 1} → {self.level}")

                self.exp = (self.exp + exp) % self.exp_cap 

                self.dmg += self.STATUS_FACTOR
                self.defense += self.STATUS_FACTOR
                self.exp_cap = self.EXP_BASE * (self.level * self.STATUS_FACTOR)
                self.health_cap = self.HEALTH_BASE + (self.level * self.STATUS_FACTOR)
                self.health = self.health_cap

            else:
                self.exp += exp