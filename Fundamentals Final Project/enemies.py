#Base enemy needs to be implemented here...
#Everything will be relational to the enum.
import character 
from enum import Enum

#This difficulty level will be chosen based on a public method that character has to see its level.
class _DifficultyLevel(Enum):
    EASY = 10,
    MEDIUM = 20,
    HARD = 30,
    EX = 50

_DifficultyLevel.EASY

class Enemy:
    def __init__(self):
        #High chance that this will NOT work as I think it will immediately
        self.difficulty_level = choose_
        character.Character.get_level()

class NormalEnemy(Enemy):
    def __init__(self):
        super().__init__()

class WeirdEnemy(Enemy):
    def __init__(self):
        super().__init__()

class GreatEnemy(Enemy):
    def __init__(self):
        super().__init__()