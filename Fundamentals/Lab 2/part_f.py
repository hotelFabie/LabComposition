# Part F
# -----1-----
game_one = {"i": 1, "title": "VHOLUME", "year": 2026, "company": "IronEqual", "genre": "Platform"}
game_two = {"i": 2, "title": "Hatsune Miku: Project DIVA", "year": 2009, "company": "HAL Laboratory", "genre": "Rhythm"}
game_three = {"i": 3, "title": "Super Monkey Ball 2", "year": 2002, "company": "Amusement Vision", "genre": "Platform"}
game_four = {"i": 4, "title": "Super Smash Bros. Ultimate", "year": 2018, "company": "HAL Laboratory", "genre": "Fighting"} 
game_five = {"i": 5, "title": "Minecraft", "year": 2009, "company": "Mojang", "genre": "Sandbox"}
game_six = {"i": 6, "title": "Persona 4 Golden", "year": 2012, "company": "Atlas", "genre": "RPG"}
game_seven = {"i": 7, "title": "Super Mario Galaxy", "year": 2006, "company": "Nintendo", "genre": "Adventure"}
game_eight = {"i": 8, "title": "Earthbound", "year": 1994, "company": "HAL Laboratory", "genre": "RPG"}

# -----2-----
games = [game_one, game_two, game_three, game_four, game_five, game_six, game_seven, game_eight]

print(games[0]['company'])

# -----3-----
#Only way I could figure to do this was through list comprehension.
#(Realized afterwards, the list isn't the catalogue in this case, so repetition was allowed.)
unique_genres = {game.get("genre") for game in games}

print(unique_genres)

# -----4-----
# Assuming nothing advanced is to be done here yet, so it'll be quite repetitive.
tuple_one = (game_one["i"], game_one["title"], game_one["year"])
tuple_two = (game_two["i"], game_two["title"], game_two["year"])
tuple_three = (game_three["i"], game_three["title"], game_three["year"])
tuple_four = (game_four["i"], game_four["title"], game_four["year"])
tuple_five = (game_five["i"], game_five["title"], game_five["year"])
tuple_six = (game_six["i"], game_six["title"], game_six["year"])
tuple_seven = (game_seven["i"], game_seven["title"], game_seven["year"])
tuple_eight = (game_eight["i"], game_eight["title"], game_eight["year"])

#Proof printing just to see that it works.
print(tuple_one)

# -----5-----
#1: Update
game_one.update({"title" : "<unknown>"})

#2 & #3: More updates 
game_five.update({"Minecraft" : "Minecraft: Bedrock Edition"})
game_five.update({"2009" : "2011"})

#4: Removal
game_one.pop("company")

#5 & 6: Nested indexing
game_two_company = games[1]["company"]
game_eight_title = games[7]["title"]

#7: Tuple retrieval
game_five_id, game_five_title, game_five_year = tuple_five

#8: Membership
is_member = "Minecraft" in games[4]["title"]
print(f"Membership status: {is_member}")
#Should give False and True above here

#9 & 10: Adding a key and 2 layer nested access
games[7]["rerelease"] = ["Wii", "3DS", "Wii U", "Switch"]
rereleases = games[7]["rerelease"]
print(rereleases)

# -----6-----
#Not printing companies, because I removed it from one, and want to be consistent.
print("<<<SUMMARY>>>")
print(f">{games[0]['title']} is a {games[0]['genre']} game, made in {games[0]['year']}")
print(f">{games[1]['title']} is a {games[1]['genre']} game, made in {games[1]['year']}")
print(f">{games[2]['title']} is a {games[2]['genre']} game, made in {games[2]['year']}")
print(f">{games[3]['title']} is a {games[3]['genre']} game, made in {games[3]['year']}")
print(f">{games[4]['title']} is a {games[4]['genre']} game, made in {games[4]['year']}")
print(f">{games[5]['title']} is a {games[5]['genre']} game, made in {games[5]['year']}")
print(f">{games[6]['title']} is a {games[6]['genre']} game, made in {games[6]['year']}")
print(f">{games[7]['title']} is a {games[7]['genre']} game, made in {games[7]['year']}")
print("<<<END OF SUMMARY>>>")
