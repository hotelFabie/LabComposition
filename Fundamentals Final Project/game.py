def start():
    # Ask user for name input. 
    # Create a character.
    pass

def menu():
    """
    Produces a menu of user actions.
    """
    print(f"CHOOSE ACTION")
    print(f"[c] : inventory")
    print(f"[w] : walk")
    print(f"[p] : profile")
    print(f"[q] : quit")
    
    choice : str = ""
    
    while (choice != "q"):
        choice = input(">")
        choice = choice.lower().strip()

        match choice:
            case "c":
                pass
            case "w":
                pass
            case "p":
                #Public method from Character
                pass