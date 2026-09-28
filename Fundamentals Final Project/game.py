import characters

def start():
    # Ask user for name input. 
    # Create a character.
    # vvvvv i think like here, you give your character 
    
    #Title
    print("಄⣀⣠MAGISTRIKE⣄⣀಄")

    character_name = input("give your character a name: ").strip().lower()
    character = characters.Character(character_name)

    #Game description for user.
    print(f"welcome [{character}] to MAGISTRIKE!\n"
          "you are but a mere traveller in this dangerous world,\n"
          "and your only way out is by starting your path.\n"
          "be careful, and be courageous!\n")
    #Test that we get what is intended

    menu()

#This will be the game loop of sorts, then. 
def menu():
    """
    Produces a menu of user actions.
    """
    print(f"಄⣀⣠ACTIONS⣄⣀಄")
    print(f"[c] : inventory")
    print(f"[w] : walk")
    print(f"[p] : profile")
    print(f"[q] : quit")
    
    choice : str = ""
    
    while (choice != "q"):
        choice = input(">>>")
        choice = choice.lower().strip()

        match choice:
            case "c":
                pass
            case "w":
                pass
            case "p":
                #Public method from Character
                pass
            default:
                #what is the python alternative
#--------------------
#Actually running the game down here.

start()