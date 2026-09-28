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
    
    #An __str__ is probably better, because it will already just format it, a getter would just get the entire object.
    #But we only want information to the user, so it wis most likely better to just format it.
    #WIP FIX...
    def __str__(self):
        return f"{self.name} [{self.difficulty.name}]"

    #They'll all need this, so maybe if we have 
    def attack(self, character : characters.Character):
        character.health -= 2
        print(f"{self.name} attacked you with 2 damage.  \\(˚☐˚”)/")

#------------------

class WeirdEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "weird enemy"

    def attack(self, character : characters.Character):
        random_damage = random.randint(0,9)
        character.health -= random_damage

        if random_damage == 0:
            print(f"{self.name} attacked you... without damaging? (° ‸ °)?")
        else:
            print(f"{self.name} attacked you with {random_damage} damage.  \\(˚☐˚”)/")

        #Thinking that this one will have some random damage thing going, making it a bit weirder.

class GreatEnemy(Enemy):
    def __init__(self, character_level):
        super().__init__(character_level)
        self.name = "great enemy"
        self.health = 20

    def attack(self, character : characters.Character):
        character.health -= 5
        print(f"{self.name} attacked you with 5 damage.  \\(˚☐˚”)/")
