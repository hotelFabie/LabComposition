#Part B

# -----1-----
numbers_with_squares = {i : i ** 2 for i in range(1,11)}

#Proof
print(numbers_with_squares)

# -----2-----
words = ["tepid", "aroma", "defuser", "apprehension", "immunity"]

words_with_length = {word : len(word) for word in words}

#Proof
print(words_with_length)

# -----3-----
possibly_duplicates = ["OMG", "WoW", "yO", "OMG", "!", "WoW"] 

unduplication_set = {word.lower() for word in possibly_duplicates}

#Proof 
print(unduplication_set)

# -----4-----
products = {
    "soap" : 5.99,
    "toothbrush" : 1.99,
    "dental floss" : 7.49,
    "deodorant" : 4.99,
    "mango body mist" : 15.99
}

cheap_products = {name : price for name, price in products.items() if price < 5}

#Proof
print(cheap_products)

# -----5-----
students = [
    {"name" : "john", "score" : 85},
    {"name" : "aubrey", "score" : 30},
    {"name" : "mackenzie", "score" : 65},
    {"name" : "jamie", "score" : 90},
    {"name" : "carson", "score" : 100}
]

graded_students = {
    student["name"] : "PASSED" if student["score"] >= 70 else "FAILED"  
    for student in students 
}

print(graded_students)