#Part A

# -----1-----
squares_normal = []

for number in range(1, 21):
    squares_normal.append(number ** 2)

squares_comprehended = [number ** 2 for number in range(1, 21)]

#Proof
print(squares_normal)
print(squares_comprehended)

# -----2-----
even_numbers = [i for i in range(1, 101) if i % 2 == 0]

#Proof
print(even_numbers)

# -----3-----
names = ["madison", "tord", "nova", "esper"]

polished_names = [name.strip().title() for name in names]

#Proof
print(polished_names)

# -----4-----
scores = [95, 20, 40, 55, 75, 60, 80, 59]

passing_scores = [score for score in scores if score >= 60]

#Proof
print(passing_scores)

#-----5-----
unlabeled_scores = [95, 20, 40, 55, 75, 60, 80, 59]

labeled_scores = [f"PASS: {score}" if score >= 60 else f"FAIL: {score}" for score in unlabeled_scores]

#Proof
print(labeled_scores)

# -----6-----
#[1] - Originally Lab 3, Part D, Question 2 : Multiplication Table
number = int(input("number: "))

multiplication_table = [number * i for i in range(1,number+1)]

#Proof
print(multiplication_table)

#[2] - Originally Lab 4, Part D, Question 6 : Active Users 
users = [
    {"username" : "enterprise78", "active" : True},
    {"username" : "jamradio39", "active" : False},
    {"username" : "21compass", "active" : True}
]

active_users = [user for user in users if user["active"]]

#Proof
print(active_users)

#[3] - Originally Lab 3, Part F, Question 2: Strings with Content
strings = ["", "hey", "hola", "hej", "", "konnichiwa", ""]

content_strings = [string for string in strings if string]

#Proof
print(content_strings)