import characters

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
                pass
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

#IMPLEMENT THE CASE FOR WALKING HERE
def walk():
    #SHOULD BE A CASE THAT YOU ENCOUNTER AN ENEMY HERE, I THINK...
    #PROBABLY THAT THE CHARACTER GETS A +1 EXP REGARDLESS OF WHAT THEY DO.

#REALLY BAD METHOD NAME, I KNOW.
def rng():
    #

#--------------------
#Actually running the game down here.

start()