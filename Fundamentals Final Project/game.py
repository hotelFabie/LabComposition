#This should probably load the user into whereever they came from.

#Should recognize state, e.g. storing things in JSON since before.
#So, either ["New Game" - n] OR ["Continue" - c]

#We will need to consider the case where the user will be below 0, then we will ask if they want to [r] : restart or [q] : quit.

def start():
    #Considering it will be able to use the menu(), 
    #And something else e.g. quit
    #It will probably only be relevant to have a reset IF we get to the point that a JSON file would be necessary.
    #Though, it could be a little excessive.
    
    #Also, they sort of need to create the character to even get to the point that they should continue.
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
    
    #can we do formatting - strip and small letters - immediately?
    #want to look up good practice for choices.
    choice : str = ""
    
    while (choice != "q"):
        choice = input(">")

        match choice:
            case "c":
                pass
            case "w":
                pass
            case "p":
                #this will probably need a method from the character. and that can be public, as long as you have the character.
                pass
                
    
    
    