import characters
import logic

def start():
    """
    Game start function, taking a name to create a character.
    Then proceeds to present a short story and options, before the game loop gets called.
    """   

    print("಄⣀⣠MAGISTRIKE⣄⣀಄")

    character_name = input("give your character a name: ").strip().lower() 
    
    while not character_name:
        print("name must consist of something other than spaces\n")
        character_name = input("give your character a name: ").strip().lower() 

    character = characters.Character(character_name)

    print("\n"
          f"welcome [{character}] to MAGISTRIKE!\n"
          "you are but a mere traveller in this dangerous world,\n"
          "and your only way out is by starting your path.\n"
          "be careful, and be courageous!\n")

    logic.menu()
    logic.action_loop(character)

#--------------------
#Actually running the game down here.

start()