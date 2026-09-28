from enum import Enum
import characters

#This difficulty level will be chosen based on a public method that character has to see its level.
class _Difficulty(Enum):
    EASY = 10
    MEDIUM = 20
    HARD = 30
    EX = 50

class Enemy:
    def __init__(self, character_level : int):
        self.difficulty : _Difficulty = self.set_difficulty(character_level)

    def set_difficulty(character_level : int) -> str:
        if character_level < 1:
            raise ValueError("Character level cannot be under 1.")
        
        new_difficulty = None

        for difficulty in _Difficulty:
            if character_level <= difficulty.value:
                new_difficulty = difficulty
                break

        return new_difficulty
    
    #An __str__ is probably better, because it will already just format it, a getter would just get the entire object.
    #But we only want information to the user, so it wis most likely better to just format it.
    def __str__(self):
        print(f"name: {self.name} difficulty: {self.difficulty}")

    #WIP: All character attributes are public, meaning that this is also seen in the game logic...
    #We'll see if it is something worth polishing later on.
    def attack(character : characters.Character):
        character.health -= 5

#Test
print(Enemy.set_difficulty(7))


#------------------

class NormalEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)

class WeirdEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)

class GreatEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)
