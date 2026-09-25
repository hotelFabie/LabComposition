#This should probably load the user into whereever they came from.

#Should recognize state, e.g. storing things in JSON since before.
#So, either ["New Game" - n] OR ["Continue" - c]



def menu():
    '''
    Produces a menu of user actions.
    '''
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
                #this will probably 
                pass
                
    
    
    