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

    def __init__(self, name : str):
        """
        Constructor method for the character.
        Get initialized with start values that can gradually go up if user levels up through game progression.
        """

        self.name : str = name
        self.level : int = 1

        self.dmg : float = self.DAMAGE_BASE

        self.main_def : float = 0
        self.temp_def : float = 0

        self.health : float = self.HEALTH_BASE
        self.health_cap : float = self.HEALTH_BASE

        self.exp : float = 0
        self.exp_cap : float = self.EXP_BASE

        self.steps = 0
        self.kills = {"normal" : 0, "weird" : 0, "great" : 0}

    def __str__(self) -> str:
        return self.name

    def get_status(self) -> str:
        """
        Gives a status overview of the player's character data and progress.
        """

        #Start of the string we'll add onto before we return.
        status = f"಄⣀⣠stats of player: [{self.name}]⣄⣀಄\n" 
        
        #Experience formatted.
        if self.level >= self.MAX_LEVEL: 
            exp_str = f"MAX"
        else:
            exp_str = f"{self.exp}/{self.exp_cap}"

        #Kills formatted.
        kills_str = ", ".join(f"{enemy}: {amount}" for enemy, amount in self.kills.items()) 
        
        status += (f"•level: {self.level} •health: {self.health}/{self.health_cap} "
            f"•damage: {self.dmg} •defense: {self.main_def} "
            f"•current exp: {exp_str}\n•kills: [{kills_str}]\n•steps taken: {self.steps}")

        return status

    def choose_action(self, enemy : enemies.Enemy) -> None:
        """
        Gives user action choices while in battle.
        Allowed actions are attacking and defending.
        Attacking: Causes damage against enemy.
        Defending: Heightens defense and heals. 
        """
        
        def assign_health() -> None:
            """
            Increases health to user within the limit of the health cap, so that it never exceeds the allowed health.
            """

            if self.health + self.HEAL > self.health_cap:
                self.health = self.health_cap
            else:
                self.health += self.HEAL

        while True:            
            print("\n•[a] attack •[d] defend")
            action = input(">")

            if (action == "a") or (action == "d"):
                break

            print("invalid input!")

        if action == "a":
            enemy.health -= self.dmg
            print(f"you attacked the enemy with {self.dmg} damage! ٩(ˋᗣˊ*)و [enemy hp: {enemy.health}]")

            if enemy.health <= 0:
                exp = enemy.difficulty.value
                assign_health()
                self.add_exp(exp)
                
                print(f"enemy defeated! gained {exp} exp.⋆⭒˚｡⋆")
                
        elif action == "d":
            assign_health()
            self.temp_def += self.STATUS_FACTOR
            print(f"you defended with {self.temp_def} defense, and healed {self.HEAL} hp! ☥")

    def add_exp(self, exp : float) -> None:
        """
        Adds experience points to the character only if they are below the max level.
        Updates the level if experience cap is reached, while increasing both the experience and health cap, plus restoring health.
        """

        def update_status():
            """
            Internal function for adjusting all status values in the case of levelling up.
            """
            self.dmg += self.STATUS_FACTOR
            self.main_def += self.STATUS_FACTOR
            self.exp_cap = self.EXP_BASE * (self.level * self.STATUS_FACTOR)
            self.health_cap = self.HEALTH_BASE + (self.level * self.STATUS_FACTOR)
            self.health = self.health_cap

        if not self.level < self.MAX_LEVEL:
            print("already max level, so no exp is gained.")
        else:
            if (self.exp + exp >= self.exp_cap):
                #In the case where you level up, stats get increased and health gets restored.
                self.level += 1
                print(f"leveled up! {self.level - 1} → {self.level}")

                self.exp = (self.exp + exp) % self.exp_cap 

                update_status()

            else:
                self.exp += exp