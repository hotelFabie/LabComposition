# Part B
# -----1-----
#Took the colors for a standard shade of turquoise.
rgb = (64, 224, 208)
r, g, b = rgb
print(r)
print(g)
print(b)

# -----2-----
person = ("Yuki", 44, "Yokohama")
name, age, city = person
print(f"{name}, {age}, {city}")

# -----3-----
#There could be a possible scenario where would have something you assume will never change,
#such as the metadata of a book.
book = ("The Best Book", 2028, "John Book")
#In a case like this, you might think afterwards "oh, I wrote the year incorrectly, let's change it".
book[1] = 2026
#While the intention of using persistent information is good, something like the line above would not work.

#Tuples are useful when you have a group of values that comprise something together,
#that would typically not make sense to change, but rather something you make a new instance of.
#Coordinates is the best argument I can think about this, if you want to store a stream of
#incoming values to track movement over time; don't change the coordinate, create a new timestamped coordinate.

# -----4-----
coordinates = [(10, 20), (255, 128), (77, 88), (50, 250)]

x_one = coordinates[1][0]
y_one = coordinates[1][1]

x_two = coordinates[3][0]
y_two = coordinates[3][1]

#Proof
print(f"x1: {x_one}, y1: {y_one}")
#Should show 255 and 128

print(f"x2: {x_two}, y2: {y_two}")
#Should show 50 and 250
