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
    #WE DO NEED SOME MORE PERMANENT VALUES AROUND HERE.
    HEALTH_BASE = 10
    #DAMAGE_BASE = ...

    def __init__(self, character_level : int):
        self.difficulty : _Difficulty = self.set_difficulty(character_level)
        self.health = self.HEALTH_BASE
        self.name = "normal enemy"
        self.damage = 2 + (self.difficulty.value / 2)

    def set_difficulty(self, character_level : int) -> str:
        
        if character_level <= 0:
            raise ValueError("ERROR: character level cannot be 0 or lower.")
        elif character_level > characters.Character.MAX_LEVEL:
            raise ValueError("ERROR: character level cannot reach above max level.")

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
    ENEMY_FACTOR = 2
    RANDOM_AMPLIFIER = 10

    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "weird enemy"

    def attack(self, character : characters.Character):
        self.damage = random.randint(0 + self.base_damage, self.RANDOM_RANGE + self.base_damage)
        super().attack(character)

class GreatEnemy(Enemy):
    DAMAGE_BASE = 5
    ENEMY_FACTOR = 2
    
    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "great enemy"
        self.health = self.HEALTH_BASE * self.ENEMY_FACTOR
        self.damage = self.DAMAGE_BASE + (self._Difficulty.value / self.DAMAGE_BASE)
