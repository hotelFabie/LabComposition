# Part E
# -----1-----
books = [
    {"title" : "The Long Book", "author" : "John Long", "pages" : 386, "available": True},
    {"title" : "Coding in C", "author" : "Amanda Cody", "pages" : 524, "available": True},
    {"title" : "Even Edges", "author" : "Blake Deep", "pages" : 100, "available": False},
    {"title" : "The Stock Plummet", "author" : "Brad Stock", "pages" : 984, "available": True},
    {"title" : "My Short Biography", "author" : "Daisy Tall", "pages" : 15, "available": False}
    ]

# -----2-----
#Title of third book
print(books[2]["title"])

#Availability of last book
print(books[-1]["available"])

# -----3-----
books[2].update({"author" : "Blake Uneven"})
books[3]["earlier_readers"] = 3

#Proof
print(books[2])
print(books[3])

# -----4-----
company = {
    "human relations" : ["Kant Hulp", "Miss Allocate"], 
    "economy" : ["Mon E. Phlow", "Caren C"], 
    "production" : ["Meda Sin", "A-Fish In-Sea"], 
    "technical support" : ["Nerde Glassmann", "Tekla Nich", "Proug Ram"], 
    "board of directors" : ["John Angry", "Josh Mad", "Lisa Angerissues"]
    }

# -----5-----
courses = [
    {"name" : "C++ and C", "teacher" : "John Pragma", "topics" : ["Data Types", "Operations", "Iteration", "Memory Management"]},
    {"name" : "Religion in East Asia", "teacher" : "Kei-san", "topics" : ["Shinto", "Buddhism", "New Age", "Abrahamitic Influence"]},
    {"name" : "The Path to Happiness", "teacher" : "Ludvig B.", "topics" : ["Games", "Meditation", "Quality Time", "Community"]}
]

#The third topic in the last made course:
print(courses[2]["topics"][2])