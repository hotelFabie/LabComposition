import characters
import enemies
import random

def menu() -> None:
    """
    Produces a menu of user actions.
    """

    print(f"಄⣀⣠ACTIONS⣄⣀಄")
    print(f"[m] : show this menu again")
    print(f"[w] : walk")
    print(f"[s] : stats")
    print(f"[t] : view task progress")
    print(f"[q] : quit")


def action_loop(character : characters.Character) -> None:
    """
    Loop for main game logic, that will continue appearing under the condition that the user does not die, nor quits.
    """

    while True:
        choice = input("\n>").lower().strip()
        match choice:
            case "m":
                menu()
            case "w":
                __walk(character)
            case "s":
                print(character.get_status())
            case "t":
                __present_tasks()
            case "q":
                print("shutting down...")
                break
            case _:
                print("not an available action.")

def __walk(character : characters.Character) -> None:
    """
    Small experience point increment per step taken.
    There is always a chance of a battle occurring.
    """

    walk_exp = 0.25
    walk_str = "step taken!"

    if character.level < character.MAX_LEVEL:
        character.exp += walk_exp
        walk_str += f" +{walk_exp}  exp.⋆⭒˚｡⋆"
    
    character.steps += 1
    print(walk_str)
    
    __possibly_cause_event(character)

def __possibly_cause_event(character : characters.Character) -> None:
    """
    2/3 pseudo-random chance that a battle is started.
    Furthermore, another pseudo-random number is generated, deciding which enemy type will be spawned.
    Biggest chance is a normal enemy. 
    """

    battle_chance_number = random.randint(1,3+1)
    if battle_chance_number == 1 or battle_chance_number == 3:
        enemy_chance_number = random.randint(1,10+1)

        if enemy_chance_number in range(1, 6+1):
            enemy = enemies.Enemy(character.level)
            __battle(character, enemy)

        elif enemy_chance_number in range(7, 8+1):
            enemy = enemies.WeirdEnemy(character.level)
            __battle(character, enemy)

        elif enemy_chance_number in range(9, 10+1):
            enemy = enemies.GreatEnemy(character.level)
            __battle(character, enemy)

def __battle(character : characters.Character, enemy : enemies.Enemy) -> None:
    """
    Takes turns between character and enemy.
    Character can either attack or defend, whereas the enemy always attacks.
    Killed enemies gets added to a counter, which can be seen with the status command outside of battle.
    """

    print(f"a {enemy} approached! battled started!")
    
    current_turn = 0

    while (enemy.health > 0):
        #Even - Character's turn
        if current_turn % 2 == 0:
            character.choose_action(enemy)

        #Odd - Enemy's turn
        else:
            enemy.attack(character)
            __check_game_over(character)
            #Remove the temporary defense after being attacked.
            character.temp_def = 0

        current_turn += 1

    character.kills[enemy.name] += 1
    __update_task(character, enemy)

def __check_game_over(character : characters.Character) -> None:
    """
    Method used in battle to check if the user's character has fainted.
    Game ends in this case, and progress will be have to be made from zero, by starting the game again.
    """

    if character.health <= 0:
        print("♰ YOU DIED : GAME OVER ♰")
        exit()

#-------------------------

#Enemy names here are for comparison to internal names of an Enemy object.
_tasks = {
    "kill_5_normals" : {"enemy_name" : "normal", "description" : "kill 5 normal enemies", "progress" : 0, "requirement" : 5, "health_increase" : 1, "completed" : False}, 
    "kill_20_normals" : {"enemy_name" : "normal", "description" : "kill 20 normal enemies", "progress" : 0, "requirement" : 20, "health_increase" : 1, "completed" : False}, 
    "kill_2_weirds" : {"enemy_name" : "weird", "description" : "kill 2 weird enemies", "progress" : 0, "requirement" : 2, "health_increase" : 1, "completed" : False},
    "kill_1_great" : {"enemy_name" : "great", "description" : "kill 1 great enemy", "progress" : 0, "requirement" : 1, "health_increase" : 1, "completed" : False},
    "kill_3_greats" : {"enemy_name" : "great", "description" : "kill 3 great enemies", "progress" : 0, "requirement" : 3, "health_increase" : 2, "completed" : False}
}

def __update_task(character : characters.Character, enemy) -> None:
    """
    Updates progress on a task. 
    If the required amount of kills for completion is accomplished, 
    the entire task is completed, and the user gets rewarded with an increased health cap.
    """

    for task in _tasks.values():
        if task["enemy_name"] == enemy.name and not task["completed"]:
            task["progress"] += 1

            #Completion scenario.
            if task["progress"] >= task["requirement"]:
                task["completed"] = True
                character.health_cap += task["health_increase"] 
                
                #Display completion.
                print(f"࣪ ˖⊹ quest [{task["description"]}] completed! ࣪ ˖⊹")

def __present_tasks() -> None:
    """
    Prepares a presentable format of all tasks that can be done, called through a menu command.
    """

    for number, task in enumerate(_tasks.values(), start=1):
        if task["completed"]:
            completion_str = "completed" 
        else:
            completion_str = f"uncompleted ({task["progress"]}/{task["requirement"]})"

        print(f"task {number}: {task["description"]} - {completion_str}")