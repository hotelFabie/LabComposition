# Part A

# -----1-----
languages = ["Python", "Go", "Java", "C++", "Rust", "C", "Ruby", "TypeScript"]
first = languages[0]
last = languages[-1]
third = languages[2]
second_to_last = languages[-2]

#Just to prove
print(f"{first} {last} {third} {second_to_last}") 

# -----2-----
#(1) First half
print(languages[:4])

#(2) Second half
print(languages[4:])

#(3) Every other, starting one ahead
print(languages[1::2])

#(4) Reverse
print(languages[::-1])

# -----3-----
languages.append("Haskell")
print(languages)

languages.insert(4, "Crystal")
print(languages)

languages.remove("Ruby")
print(languages)

languages.pop(1)
print(languages)

# -----4-----
numeric_list = [7, 2, 8, 9, 3, 6]
length = len(numeric_list)
minimum = min(numeric_list)
maximum = max(numeric_list)

#Proof
print(f"{length}, {minimum}, {maximum}")

# -----5-----

#Ascending
list_one = [5,1,3,4,2]
list_one.sort()

#Descending
list_two = [9,7,0,8,6]
list_two.sort()
list_two = list_two[::-1]

#Proof
print(f"Ascending: {list_one}")
print(f"Descending: {list_two}")

#Difference between .sort() and sorted():
#Typically, .sort() would apply sorting on an already existing list,
#whereas sorted() would produce a new sorted list out of an old one.
#That being said, you could store the new list into the same variable name if so wanted.
#E.g. list = sorted(list) 

# -----6-----

list_a = [1,2,3,4]
list_b = list_a
list_b.append(5)
print(f"List A: {list_a}, List B: {list_b}")
#They share the same reference, and so all edits on one list will happen on the other, 
#because they both point to the same part in memory.

list_b = list_a.copy()
list_b.pop()
print(f"List A: {list_a}, List B: {list_b}")
#In this case, we overwrite the old_b, but in this case it gets a shallow copy, and so they
#will NOT reference the same part in memory.