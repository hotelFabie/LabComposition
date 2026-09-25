#I am assuming already that it will be beneficial to have a map for essential logic that can be accessed at any point.

from enum import Enum

#Creation process: Define class inheriting from the Enum class.
#It seems THAT class itself is essentially ONLY for the sake of having values within it (or related method to calculate 'em)
#Should be created in a way like this, though I am not sure if I will use this terminology or not:

#These numbers do not really mean anything yet.
#BUT, this could also be a sign of using inheritance, though from something built-in this time.

#I assume to far that this will only be for internal use, as it should not really be seen by the user (externals).
#And privacy does not seem to be possible to enforce in python (if not misunderstood), so I guess we use the standard for classes?
#"class _Internal", and then these are not imported if this is to be a module.
class _DifficultyLevel(Enum):
    EASY = 10,
    MEDIUM = 20
    HARD = 30
    EX = 50