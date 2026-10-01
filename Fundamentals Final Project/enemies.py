from enum import Enum
import random
import characters

#Mapping difficulty to a number.
class _Difficulty(Enum):
    EASY = 2
    MEDIUM = 4
    HARD = 6
    EX = 8
    MASTER = 10

#Base class.
class Enemy:
    HEALTH_BASE = 10
    DAMAGE_BASE = 2

    def __init__(self, character_level : int):
        self.difficulty : _Difficulty = self.set_difficulty(character_level)
        self.health = self.HEALTH_BASE
        self.name = "normal"
        self.dmg = self.DAMAGE_BASE + (self.difficulty.value / self.DAMAGE_BASE)

    def set_difficulty(self, character_level : int) -> str:
        """
        Gives the enemy an Enum indicating its difficulty level.
        Each difficulty's value is used as comparison to the character's level, 
        ensuring that a spawned enemy scales alongside a player.
        """

        if character_level <= 0:
            raise ValueError("ERROR: character level cannot be 0 or lower.")
        elif character_level > characters.Character.MAX_LEVEL:
            raise ValueError("ERROR: character level cannot reach above max level.")

        for difficulty in _Difficulty:
            if character_level <= difficulty.value:
                assigned_difficulty = difficulty
                break

        return assigned_difficulty
    
    def __str__(self) -> str:
        """
        Enemy formatted into a string, displayed when a battle is started.
        """

        return f"{self.name} enemy [{self.difficulty.name}]"
    
    def attack(self, character : characters.Character, manual_dmg : float = 0) -> None:
        """
        Calculates damage with the user's ability to defend in consideration.
        User gets informed whether they got HP taken away or not.
        Possibility for manually adding damage is for subclasses to insert damage that is unique/RNG every turn.
        """

        if manual_dmg < 0:
            raise ValueError("cannot assign negative damage.")
        elif manual_dmg > 0:
            self.dmg = manual_dmg

        adjusted_dmg = self.dmg - (character.main_def + character.temp_def) 
        
        #Hit with damage.
        if adjusted_dmg > 0:
            character.health -= adjusted_dmg
            print(f"{self.name} attacked you with {adjusted_dmg} damage.  \\(˚☐˚”)/ [your hp: {character.health}]")
        
        #Damaged evened out.
        elif adjusted_dmg == 0: 
            print(f"{self.name} attacked you... without damaging? (° ‸ °)?")
        
        #Damage didn't pass a positive threshold.
        else:
            print("enemy's attack couldn't pierce through your strength. B-)")

#------------------

class WeirdEnemy(Enemy):
    RANDOM_RANGE : int = 7

    def __init__(self, character_level : int):
        super().__init__(character_level)
        
        self.name = "weird"

    def attack(self, character : characters.Character) -> None:
        """
        Inserts randomly generated number (within range 0-7) as damage to the method with the same name in the base class.
        Therefore, this enemy has less predictable danger.
        """

        random_dmg = random.randint(0, self.RANDOM_RANGE)
        super().attack(character, random_dmg)

#------------------

class GreatEnemy(Enemy):
    DAMAGE_BASE = 5
    GREAT_ENEMY_FACTOR = 2
    
    def __init__(self, character_level : int):
        super().__init__(character_level)

        self.name = "great"
        self.health = self.HEALTH_BASE * self.GREAT_ENEMY_FACTOR
        self.dmg = self.DAMAGE_BASE