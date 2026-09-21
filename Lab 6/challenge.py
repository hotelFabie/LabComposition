#Lab 6 Challenge

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
for p, q in zip(players, countries):
    print(f"Player: {p}, from: {q}")

#2: Numeric value focus.
for p, s, w, m in zip(players, scores, wins, matches):
    print(f"Player {p}'s statistics show that over {m} matches, they amassed {s} points, with {w} wins.")

#3: Significance (by wins), based on activity.
for p, w, a in zip(players, wins, active):
    if a: 
        active_worded = "active"
    else:
        active_worded = "inactive"
    print(f"{p} is currently {active_worded}, and has so far reached {w} wins.")

#This will cut into 3 units even when we have 4, because active - the shortest collection we've made - has 3 as length.

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

#Which players belong to Team Liquid? / 1
liquid_players = [player['name'] for player in players_cleaned if player['team'] == "Team Liquid"]

#Proof
print(f"Players belonging to Team Liquid are: {liquid_players}") 

#Which teams participate in the tournament? / 2
teams = {player['team'] for player in players_cleaned}

print(f"All the represented teams: {teams}")

#Which countries are represented WITHIN Team Liquid? / 3
liquid_countries = {player['country'] for player in players_cleaned if player['team'] == "Team Liquid"}

#Proof 
print(f"Countries represented within Team Liquid: {liquid_countries}")

#Which players have between 100 and 150 in scores?
significant_players = {player['name'] : player['score'] for player in players_cleaned if player['score'] >= 150 and player['score'] <= 200 }

#Proof
print(f"Players with a significant score (between 100 and 150): {significant_players}")

#Which inactive players reached at least a significant score?
inactive_and_significant_players = {player['name'] : player['score'] for player in players_cleaned if not player['active'] and player['score'] >= 100}

#Proof
print(f"Inactive and at least significantly scored players (minimum 100 and above: {inactive_and_significant_players}")

#:::Part 9
#Deciding the performance to be a factor calculated through: [(score / win) + (matches * 0.2)] 
#(rounded to not overwhelm with insignificant decimals)
players_extended = players_cleaned.copy()

for player in players_extended:
    player["performance"] = round((player["score"] / player["matches"]) + (player["wins"] * 0.2), 2)
        
    #Taking the proof here, while we're adding it. Why not. ¯\_(ツ)_/¯
    print(player)

#-----
#Ranking, top, threshold collection, player-to-performance mapped dict
#Preferably clear and concise transformations.
#-----

#---Ranking---
performance_sorted = sorted(players_extended, key=lambda p: p['performance'], reverse=True)

print("PLAYER PERFORMANCE RANKING (BEST TO WORST)")
for index, player in enumerate(performance_sorted, start=1):
    print(f"<{index}> {player['name']}, performance factor: {player['performance']}")

#---Top performers (say, top 3)---
print("TOP 3 PLAYERS")
for i in range(0,3):
    print(f"{i+1}. {performance_sorted[i]['name']}")

#---Above threshold of 15---
threshold_passing_players = [player for player in players_extended if player["performance"] >= 15]
print(f"TOP PERFORMERS")
for player in threshold_passing_players:
    print(f"{player['name']} with the performance factor: {player['performance']}")

#---Names mapped to performance---
performance_mapping = {player['name'] : player['performance'] for player in players_extended}

#Proof
print("NAME MAPPED TO PERFORMANCE")
for player, performance in performance_mapping.items():
    print(player, performance)

#Final Challenge
#Feels like there is a risk that some redundancy will occur here...

#Pythonic Design Challenge

#[1] First one being this:
excellent_players = [player for player in players_cleaned if player["score"] >= 200 and player["wins"] >= 50]
#... could have iterated through each player one by one and check if both conditions were passed on one "if" line.
#In that case, we would have added what passes the condition into a list either standing on its own, or being internal in a function where we return.
#List comprehension, however, is just more clean; it is literally like a sentence right now.

#[2] Second one:
players_cleaned = [
    {key : value.strip().upper() 
     if key == "name" 
     else value.title() if key == "country" 
     else value 
     for key, value in player.items()
     }
    for player in players_chaotic
]
#... could have definitely been done way more manually, by both manually writing out the key name to each value,
#but also lining up every condition a bit more extensively. Comparatively, this is not really a much shorter sequence,
#but it saves some indentation and gets to the point a little quicker. 
#Highly likely that dictionary comprehension always will be a little longer than list comprehension.
