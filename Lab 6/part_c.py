#Part C 

# -----1-----
playlist = {
    "Shunshun Shuugetsu ~ Mooned Insect" : "Team Shanghai Alice",
    "Sky Ruin" : "Team Shanghai Alice",
    "approach" : "Rei Harakami"

}

for index, (title, artist) in enumerate(playlist.items(), start=1):
    print(f"{index}. {title} - {artist}")

# -----2-----
tasks = ["Tidy the room", "Vacuum clean the kitchen", "Clean the cats' toilet", "Clean the windows neatly"]

for index, task in enumerate(tasks, start=1):
    print(f"Task {index}: {task}")

# -----3-----
values = [85, 70, 60, 50, 35, 95, 90]

for index, value in enumerate(values):
    if value >= 65:
        print(index)

# -----4-----
some_things = ["Box", "Cube", "Warp Orb", "Catapult"]

for i in range(len(some_things)):
    print(f"{i}: {some_things[i]}")

for index, thing in enumerate(some_things):
    print(f"{index}: {thing}")

#Enumeration improves readability, and you don't actually have to concern yourself with the index as much; 
#a lot of the logic seems to happen behind the scenes.