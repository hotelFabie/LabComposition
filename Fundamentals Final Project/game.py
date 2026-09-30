import characters
import enemies
import random

def menu():
    """
    Produces a menu of user actions.
    """
    print(f"಄⣀⣠ACTIONS⣄⣀಄")
    print(f"[m] : show this menu again")
    #print(f"[c] : inventory")
    print(f"[w] : walk")
    print(f"[s] : stats")
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
            case "q":
                print("shutting down...")
                break
            case _:
                print("not an available action.")

def start():
    """
    Game start function, taking a name to create a character.
    Then proceeds to present a short story and options, before the game loop gets called.
    """   
    print("಄⣀⣠MAGISTRIKE⣄⣀಄")

    character_name = input("give your character a name: ").strip().lower() 
    character = characters.Character(character_name)

    print("\n"
          f"welcome [{character}] to MAGISTRIKE!\n"
          "you are but a mere traveller in this dangerous world,\n"
          "and your only way out is by starting your path.\n"
          "be careful, and be courageous!\n")

    menu()
    action_loop(character)

def walk(character : characters.Character):
    character.steps += 1
    character.exp += 0.25
    print("step taken! +0.25 exp.⋆⭒˚｡⋆")
    possibly_cause_event(character)

#Could be smart to indicate that these are not to actually seen.
def possibly_cause_event(character : characters.Character):
    battle_chance_number = random.randint(1,3+1)
    if battle_chance_number == 1 or battle_chance_number == 3:
        #Typically, "enemy" should have something as intended?
        enemy_chance_number = random.randint(1,10+1)
        if enemy_chance_number >= 1 and enemy_chance_number <= 6:
            enemy = enemies.Enemy(character.level)
            battle(character, enemy)
        elif enemy_chance_number == 7 or enemy_chance_number == 8:
            enemy = enemies.WeirdEnemy(character.level)
            battle(character, enemy)
        elif enemy_chance_number == 9 or enemy_chance_number == 10:
            enemy = enemies.GreatEnemy(character.level)
            battle(character, enemy)

def battle(character : characters.Character, enemy : enemies.Enemy):
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
    #Some sort of append will be needed here.
    character.kills[enemy.name] += 1

def check_game_over(character : characters.Character) -> None:
    if character.health <= 0:
        print("♰ YOU DIED : GAME OVER ♰")
        exit()

#--------------------
#Actually running the game down here.

start()