#Part E

# -----1-----
words = ["jigsaw", "hammock", "trilobyte", "fume"]

def length(word):
    return len(word)

sorted_words = sorted(words, key=length)

print(sorted_words)

# -----2-----
students = [
    {"name" : "yumi", "score" : 70},
    {"name" : "xavier", "score" : 65},
    {"name" : "damian", "score" : 75},
    {"name" : "mario", "score" : 80},
    {"name" : "ryutaro", "score" : 60}
]

def score(student):
    return student["score"]

ascending_students = sorted(students, key=score)

descending_students = sorted(students, key=score, reverse=True)

#Proof 
print(ascending_students)
print(descending_students)

# -----3-----
products = [
    {"name" : "xbox one", "price" : 5000},
    {"name" : "ps5", "price" : 10000},
    {"name" : "steam deck", "price" : 12000},
    {"name" : "nintendo switch 2", "price" : 6800},
    {"name" : "gameboy advance", "price" : 2500}
]

sorted_products = sorted(products, key=lambda product:product["price"])

#Proof
print(sorted_products)

# -----4-----
names = [
    {"first_name" : "jun'ya", "last_name" : "oota"},
    {"first_name" : "masahiro", "last_name" : "sakurai"},
    {"first_name" : "satoru", "last_name" : "iwata"},
    {"first_name" : "shigeru", "last_name" : "miyamoto"}
]

sorted_names = sorted(names, key=lambda name:name["last_name"])

#Proof
print(sorted_names)

# -----5-----
word_collection = ["happy", "exhausted", "sad", "joyous", "anxious"]

def word_length(word):
    return len(word)

sorted_one = sorted(word_collection, key=word_length)
sorted_two = sorted(word_collection, key=lambda word:len(word))

#Proof
print(sorted_one)
print(sorted_two)

#While this is a very simple example, function used as a key - in my opinion - makes it clearer in simple cases.
#Lambda here does not benefit the readability, but it would be beneficial if it was a more complex case where it can't 
#be described properly with just like three words fitting into a variable.
#It really seems to depend on how deep and many conditions that will be applied, but generally I'd like
#to think that a function should have a descriptive name to begin with, so I'd often lean towards functions over lambda.