import characters
import enemies
import items
import random

#Shield. Sword, Heart
_store = []

def menu():
    """
    Produces a menu of user actions.
    """
    print(f"಄⣀⣠ACTIONS⣄⣀಄")
    print(f"[m] : show this menu again")
    print(f"[w] : walk")
    print(f"[s] : stats")
    print(f"[b] : buy items")
    print(f"[q] : quit")


def action_loop(character : characters.Character):
    """
    Loop for main game logic, that will continue appearing under the condition that the user does not die, nor quits.
    """
    choice : str = ""

    while (choice != "q"):
        choice = input("\n>")
        choice = choice.lower().strip()

        match choice:
            case "m":
                menu()
            case "w":
                walk(character)
            case "s":
                print(character.get_status())
            case "b":
                store()
            case "q":
                print("shutting down...")
                break
            case _:
                print("not an available action.")


def walk(character : characters.Character):
    """
    Small experience point increment per step taken.
    There is always a chance of a battle occurring.
    """
    walk_exp = 0.25
    
    character.steps += 1
    character.exp += walk_exp
    print(f"step taken! +{walk_exp} exp.⋆⭒˚｡⋆")
    
    possibly_cause_event(character)

#Could be smart to indicate that these are not to actually seen.
def possibly_cause_event(character : characters.Character):
    """
    2/3 pseudo-random chance that a battle is started.
    Furthermore, another pseudo-random number is generated, deciding which enemy type will be spawned.
    Biggest chance is a normal enemy. 
    """
    battle_chance_number = random.randint(1,3+1)
    if battle_chance_number == 1 or battle_chance_number == 3:
        #Typically, "enemy" should have something as intended?
        enemy_chance_number = random.randint(1,10+1)

        if enemy_chance_number in range(1, 6+1):
            enemy = enemies.Enemy(character.level)
            battle(character, enemy)

        elif enemy_chance_number in range(7, 8+1):
            enemy = enemies.WeirdEnemy(character.level)
            battle(character, enemy)

        elif enemy_chance_number in range(9, 10+1):
            enemy = enemies.GreatEnemy(character.level)
            battle(character, enemy)

def battle(character : characters.Character, enemy : enemies.Enemy):
    """
    Takes turns between character and enemy.
    Character can either attack or defend, whereas the enemy always attacks.
    Killed enemies gets added to a counter, which can be seen with the status command outside of battle.
    """
    print(f"a {enemy} approached! battled started!")
    
    current_turn = 0

    while (enemy.health > 0):
        if current_turn % 2 == 0:
            character.choose_action(enemy)

        else:
            enemy.attack(character)
            check_game_over(character)
            character.temp_def = 0

        current_turn += 1

    character.kills[enemy.name] += 1

def check_game_over(character : characters.Character) -> None:
    """
    Method used in battle to check if the user's character has fainted.
    Game ends in this case, and progress will be have to be made from zero, by starting the game again.
    """
    if character.health <= 0:
        print("♰ YOU DIED : GAME OVER ♰")
        exit()

#def store():
_store 
#i think this should have a list, and we transfer it back and forth. 