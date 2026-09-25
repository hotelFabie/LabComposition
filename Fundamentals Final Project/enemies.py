#Base enemy needs to be implemented here...
#Everything will be relational to the enum.
from enum import Enum

#This difficulty level will be chosen based on a public method that character has to see its level.
class _Difficulty(Enum):
    EASY = 10
    MEDIUM = 20
    HARD = 30
    EX = 50

#What if instead, we give it the player's difficulty level as input - dependency injection - and then compare it to the difficulty level?
#There maybe probably not be any cleaner way than simply comparing, and I assume that we can do it on the actual name itself?

class Enemy:
        #I assume this is str
    def __init__(self, character_level : int):
        #High chance that this will NOT work as I think it will immediately
        self.difficulty : _Difficulty = self.set_difficulty(character_level)

    def set_difficulty(character_level : int) -> str:
        new_difficulty = None

        #Not sure if a ValueError will need to pop up here.

        for difficulty in _Difficulty:
            #This logic is not done.
            if character_level <= difficulty.value:
                new_difficulty = difficulty

        return new_difficulty

    #Either a __str__ or a getter method.

    #Test

print(Enemy.set_difficulty(50))


#------------------

class NormalEnemy(Enemy):
    def __init__(self):
        super().__init__()

class WeirdEnemy(Enemy):
    def __init__(self):
        super().__init__()

class GreatEnemy(Enemy):
    def __init__(self):
        super().__init__()