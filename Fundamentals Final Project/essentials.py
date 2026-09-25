#I am assuming already that it will be beneficial to have a map for essential logic that can be accessed at any point.

from enum import Enum

#Starting to think that maybe this would be better for use of the enemy. 
#So that this would exist in realtion to the enemy.
class _DifficultyLevel(Enum):
    EASY = 10,
    MEDIUM = 20
    HARD = 30
    EX = 50