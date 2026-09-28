import characters

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

def action_loop(character : characters.Character):
    #Probably best to isolate this into its own separate loop.
    choice : str = ""

    #A bit unsure about how this is intended to be.
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
#--------------------
#Actually running the game down here.

start()