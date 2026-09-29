from enum import Enum
import random
import characters

#This difficulty level will be chosen based on a public method that character has to see its level.
class _Difficulty(Enum):
    EASY = 3
    MEDIUM = 5
    HARD = 7
    EX = 10

#Thought about this being an abstract class, but we haven't been going through that.
class Enemy:
    def __init__(self, character_level : int):
        self.difficulty : _Difficulty = self.set_difficulty(character_level)
        #Just to make sure that it works.
        self.health = 10
        self.name = "normal enemy"

    def set_difficulty(self, character_level : int) -> str:
        if character_level < 1:
            raise ValueError("character level cannot be under 1.")
        
        new_difficulty = None

        for difficulty in _Difficulty:
            if character_level <= difficulty.value:
                new_difficulty = difficulty
                break

        return new_difficulty
    
    def __str__(self):
        return f"{self.name} [{self.difficulty.name}]"

    #This behavior is how I intend it, but the weird enemy's random damage makes this logic a bit hard to transfer.
    def attack(self, character : characters.Character):
        damage = 2 
        if not damage - character.defense < 0:
            character.health - damage
            print(f"{self.name} attacked you with {damage} damage.  \\(˚☐˚”)/")
        else:
            print("enemy's attack couldn't pierce through your strength. B-)")

#------------------

class WeirdEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "weird enemy"

    def attack(self, character : characters.Character):
        random_damage = random.randint(0,9) - character.defense
        character.health -= random_damage - character.defense

        if random_damage == 0:
            print(f"{self.name} attacked you... without damaging? (° ‸ °)?")
        else:
            print(f"{self.name} attacked you with {random_damage} damage.  \\(˚☐˚”)/")

class GreatEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "great enemy"
        self.health = 20

    def attack(self, character : characters.Character):
        character.health -= 5 - character.defense
        print(f"{self.name} attacked you with 5 damage.  \\(˚☐˚”)/")
