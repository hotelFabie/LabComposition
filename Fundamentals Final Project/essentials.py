#I am assuming already that it will be beneficial to have a map for essential logic that can be accessed at any point.

from enum import Enum

#Creation process: Define class inheriting from the Enum class.
#It seems THAT class itself is essentially ONLY for the sake of having values within it (or related method to calculate 'em)
#Should be created in a way like this, though I am not sure if I will use this terminology or not:

#These numbers do not really mean anything yet.
class DifficultyLevel(Enum):
    EASY = 10,
    MEDIUM = 20
    HARD = 30
    EX = 50