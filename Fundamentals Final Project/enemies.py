from enum import Enum
import characters

#This difficulty level will be chosen based on a public method that character has to see its level.
class _Difficulty(Enum):
    EASY = 3
    MEDIUM = 5
    HARD = 7
    EX = 10

class Enemy:
    def __init__(self, character_level : int):
        self.difficulty : _Difficulty = self.set_difficulty(character_level)
        #Just to make sure that it works.
        self.health = 10
        self.name = "enemy"

    def set_difficulty(self, character_level : int) -> str:
        if character_level < 1:
            raise ValueError("character level cannot be under 1.")
        
        new_difficulty = None

        for difficulty in _Difficulty:
            if character_level <= difficulty.value:
                new_difficulty = difficulty
                break

        return new_difficulty
    
    #An __str__ is probably better, because it will already just format it, a getter would just get the entire object.
    #But we only want information to the user, so it wis most likely better to just format it.
    #WIP FIX...
    def __str__(self):
        return f"{self.name} [{self.difficulty.name}]"

    #WIP: All character attributes are public, meaning that this is also seen in the game logic...
    #We'll see if it is something worth polishing later on.
    def attack(self, character : characters.Character):
        character.health -= 2
        print(f"{self.name} attacked you with 2 damage.  \\(˚☐˚”)/")

#------------------

class NormalEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "normal enemy"

class WeirdEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "weird enemy"

class GreatEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "great enemy"
