# MAGISTRIKE : A TURN-BASED RPG

## About 
Magistrike is a turn-based game, with the goal of surviving as long as possible.
You encounter different enemies - normal, weird, and great.
Keep fighting and try to survive, while improving your stats as you level up.
Essentially an endless game until you die.

## Main functionality 
### Essentials
The main mechanic is quite simple, which is the walk command. You gain a small amount of EXP each time you take a step.
Every time you walk, there is a pseudo-random chance of encountering one of three enemies (inheritance structure). 

Enemy encounters causes a battle to start, where you as the player have two choices.
1. **A**: Attack the enemy. 
2. **D**: Defend, increasing health and defense. Depending on stats, you may block the enemy damage entirely.

The battle continues until either the enemy or you die, with the latter resulting in a GAME OVER.
Winning a battle results in an EXP increase. 
Reaching the current EXP cap makes you level up, which improves stats - damage, defense, health cap - just a little bit.

#### Note
For the character and enemy to be able to attack each other, attributes are visible for both.

### Peripherals
While walking is the main mechanic to make something happen,
it is one of a few choices presented in the game's menu.
- **Show menu again**.
- **Overview** of character's **current statistics**. Can be used as an indicator between battles how defensive to be to maintain the health.
- **Task overview**. There are 5 tasks activated from the beginning, which reward the user with a slightly increased health cap if accomplished. All tasks focus on killing a certain amount of one type of enemy.
- **Quit**. As data is not persistent in this game, your progress will not have been saved when you start again.

## How to run
Run <code>python game.py</code> to start the game in a terminal on the same directory. 
Start by giving a character name.