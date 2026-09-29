from enum import Enum
import random
import characters

class _Difficulty(Enum):
    EASY = 3
    MEDIUM = 6
    HARD = 9
    EX = 12
    MASTER = 15

class Enemy:
    def __init__(self, character_level : int):
        self.difficulty : _Difficulty = self.set_difficulty(character_level)
        self.health = 10
        self.name = "normal enemy"
        self.damage = 2 + (self.difficulty.value / 2)

    def set_difficulty(self, character_level : int) -> str:
        
        if character_level < 1:
            raise ValueError("ERROR: character level cannot be under 1.")
        elif character_level > 15:
            raise ValueError("ERROR: character level cannot reach above max level (15).")

        for difficulty in _Difficulty:
            if character_level <= difficulty.value:
                new_difficulty = difficulty
                break

        return new_difficulty
    
    def __str__(self):
        return f"{self.name} [{self.difficulty.name}]"
    
    #This behavior is how I intend it, but the weird enemy's random damage makes this logic a bit hard to transfer.
    def attack(self, character : characters.Character):
        adjusted_damage = self.damage + (self.difficulty.value / 2) - (character.defense + character.temporary_defense) 
        if adjusted_damage > 0:
            character.health -= adjusted_damage
            print(f"{self.name} attacked you with {adjusted_damage} damage.  \\(˚☐˚”)/")
        elif adjusted_damage == 0: 
            print(f"{self.name} attacked you... without damaging? (° ‸ °)?")
        else:
            print("enemy's attack couldn't pierce through your strength. B-)")


#------------------

class WeirdEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "weird enemy"
        #Should grow in relation to their level.
        self.base_damage = 0
        self.damage = 0

    def attack(self, character : characters.Character):
        self.damage = random.randint(0 + self.base_damage, 9 + self.base_damage)
        super().attack(character)

class GreatEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "great enemy"
        self.health = 20
        self.damage = 5 + (self.difficulty.value / 2)
