#THIS IS NOT FINISHED YET, AS THIS IS AN EXTRA ASSIGNMENT.

#:::Part 1
players_chaotic = [
    {"name" : "  ReKKLez ", "team" : "Fnatic", "country" : "SwEDen", "score": 150, "matches" : 47, "wins" : 24, "active" : False},
    {"name" : "xPeKE", "team" : "Fnatic", "country" : "spaIN", "score": 165, "matches" : 47, "wins" : 24, "active" : False},
    {"name" : "fAKER", "team" : "T1", "country" : "South koREa", "score": 300, "matches" : 131, "wins" : 101, "active" : True},
    {"name" : "      TenZ   ", "team" : "T1", "country" : "Canada", "score": 265, "matches" : 125, "wins" : 75, "active" : True},
    {"name" : "SuGArZ3ro  ", "team" : "ZERO DIVISION", "country" : "Japan", "score": 15, "matches" : 5, "wins" : 0, "active" : True},
    {"name" : "    SHAKA", "team" : "ZERO DIVISION", "country" : "JApan", "score": 223, "matches" : 90, "wins" : 58, "active" : True},
    {"name" : "s1MplE", "team" : "BC.Game Esports", "country" : "Ukraine", "score": 240, "matches" : 101, "wins" : 76, "active" : False},
    {"name" : "MaGISK", "team" : "BC.Game Esports", "country" : "DenmArk", "score": 28, "matches" : 10, "wins" : 0, "active" : True},
    {"name" : "HoOXi", "team" : "Astralis", "country" : "DENmark", "score": 113, "matches" : 64, "wins" : 35, "active" : True},
    {"name" : " phZy  ", "team" : "Astralis", "country" : "Sweden", "score": 15, "matches" : 3, "wins" : 0, "active" : True},
    {"name" : "Zer0", "team" : "Team Liquid", "country" : "AustRAlia", "score": 210, "matches" : 135, "wins" : 85, "active" : False},
    {"name" : " MeNdo", "team" : "Team Liquid", "country" : "sWEDEn", "score": 155, "matches" : 90, "wins" : 42, "active" : True},
    {"name" : "PIStillo         ", "team" : "Team Liquid", "country" : "MeXIco", "score": 20, "matches" : 8, "wins" : 0, "active" : False},
    {"name" : "CaPs   ", "team" : "G2 Esports", "country" : "Denmark", "score": 95, "matches" : 85, "wins" : 37, "active" : True},
    {"name" : "   HaNs SaMA", "team" : "G2 Esports", "country" : "France", "score": 101, "matches" : 74, "wins" : 28, "active" : True},
]

#:::Part 2

    # Realized you do not need to write out everything manually, just take everything and then do conditionals for
    # scenarios we are concerned about. So skip sh*t like this.
    # {"name" : player["name"].strip().upper(), 
    #  "team" : player["team"], 
    #  "country" : player["country"].title(),
    #  "score" : player["score"], 
    #  "matches" : player["matches"], 
    #  "wins" : player["wins"], 
    #  "active" : player["active"]}

players_cleaned = [
    {key: value.strip().upper() 
     if key == "name" 
     else value.title() if key == "country" 
     else value 
     for key, value in player.items()
     }
    for player in players_chaotic
]

#Proof
print(players_cleaned)

#:::Part 3

#Active players
active_players = [player for player in players_cleaned if player["active"]]

#Proof
print(active_players)

#Players with at least 3 wins
wins_3_players = [player for player in players_cleaned if player["wins"] >= 3]

#Proof
print(f"Players with at least 3 wins: {wins_3_players}")

#Players with a score that is at least 80
score_150_players = [player for player in players_cleaned if player["score"] >= 150]

#Proof
print(f"Players with at least 150 in score: {score_150_players}")

#Swedish players
swedish_players = [player for player in players_cleaned if player["country"] == "Sweden"]

#Proof
print(f"Swedish players: {swedish_players}")

#Players meeting two conditions that can be arguable seen as an excellent status.
excellent_players = [player for player in players_cleaned if player["score"] >= 200 and player["wins"] >= 50]

#Proof
print(f"Excellent players: {excellent_players}")

#In my opinion, all of these cases are more easily read with list comprehension.

#:::Part 4

#All unique countries
represented_countries = {player["country"] for player in players_cleaned}

#Proof
print(f"All participating countries: {represented_countries}")

#All unique teams
represented_teams = {player["team"] for player in players_cleaned}

#Proof
print(f"All participating teams: {represented_teams}")

#Players and their scores
players_and_scores = {player["name"] : player["score"] for player in players_cleaned}

#Proof
print(players_and_scores)

#Players and their wins
#dictionary comprehensions
players_and_wins = {player["name"] : player["wins"] for player in players_cleaned}

#Proof
print(players_and_wins)

#Players in a score threshold
#dictionary comprehension, 150 points
players_and_150_scores = {player["name"] : player["score"] for player in players_cleaned if player["score"] >= 150}

#Proof
print(players_and_150_scores)

#:::Part 5
players = ["TeSeS", "NiKo", "kyxsan", "m0NESY"]

scores = [130, 210, 160, 110]

countries = ["Denmark", "Bosnia", "North Macedonia", "Russia"]

wins = [57, 83, 46, 36]

matches = [92, 112, 95, 70]

active = [False, True, False]

#1: Simple origin information, tuple contained.
basic_info = [(p, q) for p, q in zip(players, countries)] 

#Proof
print("BASIC INFO")
print(f"Combination 1: {basic_info}")

b1, b2, b3, b4 = basic_info

#2: Numericals, dictionary contained.
numerical_info = [
    {"player" : p,
    "score" : s,
    "wins" : w,
    "matches" : m} 
    for p, s, w, m in 
    zip(players, scores, wins, matches)
]

n1, n2, n3, n4 = numerical_info

#Proof
print("NUMERICALS")
print(f"Combination 2: {numerical_info}")

#3: Remarks: Who they are, how much they've won, and if they're still active in the scene.
remarks = [
    (p,w,a)
    for p, w, a in
    zip(players, wins, active)
]

#This will cut into 3 units even when we have 4, because active - the shortest collection we've made - has 3 as length.

r1, r2, r3 = remarks

#Proof
print("REMARKS")
print(f"Remark one: {r1}, Remark two: {r2}, Remark three: {r3}")

#In this case, I mostly saw the unpacking the results as just getting each player out as their own unit.
#Easier to zip it together, so naming the unpacked variables was a bit difficult.
#They simply got [letter+number]; didn't want to get hooked on this part for too long.

#:::Part 6

#---Most wins---
wins_ordering = sorted(players_cleaned, key=lambda a: a['wins'], reverse=True)

print("MOST WINS")
for index, player in enumerate(wins_ordering, start=1):
    print(f"[{index}] {player['name']} - {player['wins']}")

#---Highest score---
def order_scores(player):
    return player['score']

score_ordering = sorted(players_cleaned, key=order_scores, reverse=True)

print("HIGHEST SCORE")
for index, player in enumerate(score_ordering, start=1):
    print(f"[{index}] {player['name']} - {player['wins']}")

#Most matches played
def order_matches(player):
    return player['matches']

match_ordering = sorted(players_cleaned, key=order_matches)

#this one should not have reverse ordering, it will be the only one ascending
print("MATCHES")
for index, player in enumerate(match_ordering, start=-len(match_ordering)):
    print(f"[{abs(index)}] {player['name']} - {player['matches']}")

#Player name alphabetically
alphabetical_ordering = sorted(players_cleaned, key=lambda a: a['name'])

print("ALPHABETICAL ORDERING")
for index, player in enumerate(alphabetical_ordering, start=1):
    print(f"[{index}] {player['name']}")

#:::Part 7
#Reusing the sorting from Part 6, because it is already "provided".
for index, player in enumerate(score_ordering, start=1):
    print(f"{index}. {player['name']} - {player['score']} points")

#:::Part 8
#It feels a bit like this question is just a rephrasing of Part 4.

#Which players belong to Team Liquid?
liquid_players = [player['name'] for player in players_cleaned if player['team'] == "Team Liquid"]

#Proof
print(f"Players belonging to Team Liquid are: {liquid_players}") 

#Which teams participate in the tournament?
teams = {player['team'] for player in players_cleaned}

print(f"All the represented teams: {teams}")

#Which countries are represented WITHIN Team Liquid?
liquid_countries = {player['country'] for player in players_cleaned if player['team'] == "Team Liquid"}

#Proof 
print(f"Countries represented within Team Liquid: {liquid_countries}")

#Which players belong to BC.Game Esports?
bc_players = {key : value for player.items() in players_cleaned if player['team'] == "BC.Game Esports"}

#AT LEAST 5, SO CREATE ANOTHER QUESTION ON MY OWN.

#:::Part 9