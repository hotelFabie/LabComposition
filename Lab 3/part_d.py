# Part D
# -----1-----
count = 10
for i in range(10):
    print(count - i)
    
# -----2-----
#Was not specified if the limit is 10 or itself, so I went with [itself]
number = int(input("number: "))

multiplication_table = []
for i in range(1, number + 1, 1):
    table_part = i * number
    multiplication_table.append(table_part)

print(f"multiplication table for {number}")

print(multiplication_table)

# -----3-----
playlist = [
    {"artist" : "CAPSULE", "title" : "テレポテーション"},
    {"artist" : "The GazettE", "title" : "Shiver"},
    {"artist" : "Rei Harakami" , "title" : "bioscope"},
    {"artist" : "Akira Yamaoka" , "title" : "Fever Chill"}
]

for index, song in enumerate(playlist):
    print(f"{index + 1}. {song['artist']} - {song['title']}")
    
# -----4-----
for i in range(3):
    for j in range(4):
        print(f"(x: {i+1}, y: {j+1})")
        
# -----5-----
for i in range(5):
    row = ""

    for j in range(5):
        row += "x"

    print(row)            