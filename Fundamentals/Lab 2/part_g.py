# Part G
# -----1-----
list_one = ["jasonhouse83",  "ghostberry", "7chrisgreen", "lucyarts", "mahogany"]
list_two = [ "jasonhouse83", "7chrisgreen", "lucyarts", "raindropped", "99noir"]

duplicates = set(list_one) & set(list_two)
print(duplicates)

uniques_one = set(list_one) - set(list_two)
uniques_two = set(list_two) - set(list_one)
print(f"Unique to [1]: {uniques_one}, unique to [2]: {uniques_two}")

# -----2-----
online_course = {
    "courses" : ["math", "chemistry"],
    "teachers" : ["marla", "jason"],
    "students" : ["jennifer", "paula", "hugo"],
    "topics" : ["integrals", "discrete numbers", "biomolecular study", "analysis of microscopical images"]
}

# -----3-----
inventory = {
    "tennis ball" : 153,
    "racket" : 51,
    "shoes" : 42,
    "sports drink" : 39,
    "protein bar" : 13,
}

inventory["protein bar"] += 10
inventory["tennis ball"] -= 15

total_units = sum(inventory.values())

#Proof of contents
print(inventory)
print(total_units)

# -----4-----
#TUPLES AND LISTS
#Both tuples and lists are indexable collections, with the difference that tuples are persistent.
#Lists are good for sorting purposes, tuples are good for "permanent" data like timestamps with location data.

#DICTIONARIES AND SETS
#Dictionaries can be seen as indexing BUT not in order, but rather on a value that is a "key".
#It is beneficial where you want to quickly store related information under one (umbrella) term.

#Lastly, sets are, in my opinion, the most unique, and literally only care about unique values.
#They are good when you don't care about quantities, but rather just storing that something exists 
#within a category.