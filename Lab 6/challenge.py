#THIS IS NOT FINISHED YET, AS THIS IS AN EXTRA ASSIGNMENT.

#Part 1
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
    {"name" : " phZy  ", "team" : "Astralix", "country" : "Sweden", "score": 15, "matches" : 3, "wins" : 0, "active" : True},
    {"name" : "Zer0", "team" : "Team Liquid", "country" : "AustRAlia", "score": 210, "matches" : 135, "wins" : 85, "active" : False},
    {"name" : " MeNdo", "team" : "Team Liquid", "country" : "sWEDEn", "score": 155, "matches" : 90, "wins" : 42, "active" : True},
    {"name" : "PIStillo         ", "team" : "Team Liquid", "country" : "MeXIco", "score": 20, "matches" : 8, "wins" : 0, "active" : False},
    {"name" : "CaPs   ", "team" : "G2 Esports", "country" : "Denmark", "score": 95, "matches" : 85, "wins" : 37, "active" : True},
    {"name" : "   HaNs SaMA", "team" : "G2 Esports", "country" : "France", "score": 101, "matches" : 74, "wins" : 28, "active" : True},
]

#Part 2

    # Realized you do not need to write out everything manually, just take everything and then do conditionals for
    # scenarios we are concerned about. So skip sh*t like this.
    # {"name" : player["name"].strip().upper(), 
    #  "team" : player["team"], 
    #  "country" : player["country"].title(),
    #  "score" : player["score"], 
    #  "matches" : player["matches"], 
    #  "wins" : player["wins"], 
    #  "active" : player["active"]}

players = [
    {key: value.strip().upper() 
     if key == "name" 
     else value.title() if key == "country" 
     else value 
     for key, value in player.items()
     }
    for player in players_chaotic
]

#Proof
print(players)

#Part 3
