import characters
import enemies
#import items
import random

#WIP: Maybe that this is to be renamed to "logic", and we have some other place to run all of this.

#All the core parts for actually running everything is here below.
#----------
def menu():
    """
    Produces a menu of user actions.
    """
    print(f"಄⣀⣠ACTIONS⣄⣀಄")
    print(f"[m] : show this menu again")
    print(f"[c] : inventory")
    print(f"[w] : walk")
    print(f"[p] : profile")
    print(f"[q] : quit")


def action_loop(character : characters.Character):
    choice : str = ""

    while (choice != "q"):
        choice = input(">")
        choice = choice.lower().strip()

        match choice:
            case "m":
                menu()
            case "c":
                pass
            case "w":
                walk(character)
            case "p":
                #Public method from Character
                print(character.get_profile())
            case "q":
                print("shutting down...")
                break
            case _:
                print("not an available action.")

def start():    
    #Title
    print("಄⣀⣠MAGISTRIKE⣄⣀಄")

    character_name = input("give your character a name: ").strip().lower() 
    character = characters.Character(character_name)

    #Game description for user.
    print("\n"
          f"welcome [{character}] to MAGISTRIKE!\n"
          "you are but a mere traveller in this dangerous world,\n"
          "and your only way out is by starting your path.\n"
          "be careful, and be courageous!\n")

    menu()
    action_loop(character)

#Everything related to the action: [w] walk
def walk(character : characters.Character):
    character.exp += 0.25
    print("\r +0.25 exp.⋆⭒˚｡⋆")
    possibly_cause_event(character)

#Could be smart to indicate that these are not to actually seen.
def possibly_cause_event(character : characters.Character):
    battle_chance_number = random.randint(1,3+1)
    if battle_chance_number == 1:
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
    #Considering that we have another case, being or 2 or 3, depends e.g. if items are to be implemented.

def battle(character : characters.Character, enemy : enemies.Enemy):
    print(f"a {enemy} approached! battled started!")
    
    current_turn = 0

    while (enemy.health > 0):
        if current_turn % 2 == 0:
            character.choose_action(enemy)
        else:
            enemy.attack(character)
        current_turn += 1

#--------------------
#Actually running the game down here.

start()