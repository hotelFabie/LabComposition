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
        choice = input("action>")
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
    # Ask user for name input. 
    # Create a character.
    # vvvvv i think like here, you give your character 
    
    #Title
    print("಄⣀⣠MAGISTRIKE⣄⣀಄")

    character_name = input("give your character a name: ").strip().lower()
    #This one must exist outside, so 
    character = characters.Character(character_name)

    #Game description for user.
    #it wraps it in double brick parentheses here... i wonder why...
    print("\n"
          f"welcome [{character}] to MAGISTRIKE!\n"
          "you are but a mere traveller in this dangerous world,\n"
          "and your only way out is by starting your path.\n"
          "be careful, and be courageous!\n")
    #Test that we get what is intended

    menu()
    action_loop(character)


#Everything related to the action: [w] walk
def walk(character : characters.Character):
    #should have a text indicator about what is happening...
    possibly_cause_event(character)
    character.exp += 1

#Could be smart to indicate that these are not to actually seen.
def possibly_cause_event(character : characters.Character):
    random_number = random.randint(1,3+1)
    if random_number == 1:
        #WIP: Should not always be a NormalEnemy.
        enemy = enemies.NormalEnemy(character.level)
        battle(character, enemy)

def battle(character : characters.Character, enemy : enemies.Enemy):
    print(f"a {enemy} approached! battled started!")
    
    current_turn = 0
    #Main player
    while (enemy.health > 0):
        if current_turn % 2 == 0:
            character.choose_action()
        else:
            enemy.attack(character)

#probably need some level_up logic as well.

#--------------------
#Actually running the game down here.

start()