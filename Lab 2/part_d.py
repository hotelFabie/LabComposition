# Part D
# -----1-----
laptop = {"brand": "Lenovo", "model": "Legion", "RAM": "8GB", "storage": "512GB", "price": 579.99}

# -----2-----
#Update the price
laptop.update({"price" : 489.99})

#Add operating system key
laptop["operating_system"] = "Linux"

#Remove one key
laptop.pop("model")

#Proof
print(laptop)

# -----3-----

#Existing key
laptop.get("operating_system")

#Missing key - now deleted since before
laptop.get("model")

#Conceptual comparison:
#While both direct indexing and accessing through key is a means to get a value, you'll see that:
laptop.get("")
#^ Does not about where it is located in the collection, just that we want this specific thing.
#v This, however, is concerned about the position, not meaning we probably have an idea of 
#v what this collections' elements all represent:
apples = ["Fuji", "Granny Smith", "Pink Lady"]
second_apple = apples[1]


# -----4-----
print(laptop.keys())
print(laptop.values())
print(laptop.items())

# -----5-----
courses = {"mathematics" : 45, "physics" : 70, "cooking" : 25, "quantum computing" : 95, "meditation and spiritualism" : 10, }
total_hours = sum(courses.values())
print(total_hours)