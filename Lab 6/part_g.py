#Part G

# -----1-----
multiple_nums = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

#Honestly took a while, because I misinterpreted what n and nums is seen as per iteration until I wrote it down on paper.
single_nums = [n for nums in multiple_nums for n in nums]

#Proof
print(single_nums)

# -----2-----
#Presuming we want an input, like earlier assignments, before creating it.
limit = int(input("give a number limit: "))

multiplication_table = [
    [j*i for j in range(1, i+1)]
    for i in range(1, limit+1)
]

#Proof
print(multiplication_table)

#I think that the +1 in the ranges make it slightly less unreadable,
#otherwise I think it would have been relatively understandable
#(that the multiplication per number "i" never stretches beyond itself ("j" in relation to what "i" is)).

#A bit tricky maybe in the start, but if you're already familiar with 
#nested for loops, it might just look a bit backwards, and that's all.

# -----3-----
names = ["Jameson", "Aubrey", "Travis", "Mila", "Kumar", "Ishmael"]
scores = [60, 75, 80, 65, 90, 50]

passing_students = [
    {"name" : name, "score" : score} 
    for name, score in zip(names, scores) 
    if score >= 70
]

#Proof
print(passing_students)

# -----4-----
#first solve with loops, not loop comprehension
more_scores = [50, 70, 90, 40, 55, 65, 75, 85, 95]

#[With for loops]
#1. If anyone got over 90 points (in this case, that is a high grade)
def any_amazing_score(scores : list) -> bool:
    for score in scores:
        if score >= 90:
            return True 
    return False

#2. If everyone passed the acceptable limit of 60 points
def all_passing_scores(scores : list) -> bool:
    for score in scores:
        if not score >= 60:
            return False
    return True

#Should give True and False
print(f"Q1: {any_amazing_score(more_scores)}")
print(f"Q2: {all_passing_scores(more_scores)}")

#[With any() and all()]
#1. If anyone got over 90 points (in this case, that is a high grade)
has_amazing_score = any([score >= 90 for score in more_scores])
#2. If everyone passed the acceptable limit of 60 points
has_everyone_passed = all([score >= 60 for score in more_scores])

#Also gives True and False
print(f"Q1: {has_amazing_score}")
print(f"Q2: {has_everyone_passed}")

# -----5-----
#[1] List Comprehension : Fewer lines for same action as a for loop iteration of a list
employees = [
    {"name" : "Janet", "age": 60},
    {"name" : "Marilyn", "age": 23},
    {"name" : "Monica", "age": 54},
    {"name" : "Tanya", "age": 27},
]

older_employees = [employee for employee in employees if employee["age"] >= 50]

#Proof
print(older_employees)

#[2] Unpacking : Not needing to look at every single index to assign multiple variables
rgb = (51, 51, 255)
r, g, b = rgb

#Proof
print(f"R: {r}, G: {g}, B: {b}")

#[3] Swapping : Not needing an intermediary temporary variable, super readable
pole_one = "Positive"
pole_two = "Negative"
pole_one, pole_two = pole_two, pole_one

#Proof
print(pole_one, pole_two)

#[4] Set Operations : Does not require explicit method calling, really has both sentence- and math-like structure
climbers = {"jake", "madison", "ashley", "drew", "carly"}
bowlers = {"jake", "mason", "aaron", "britney", "ashley"}

common_people = climbers & bowlers

#Proof
print(f"Both climbers and bowlers: {common_people}")

#[5] Lambda : Useful in areas where you don't want to create and insert a function, but rather just do a short operation 
#right where the main logic is happening.
numbers = [1, 2, 3, 4]

squares = list(map(lambda n : n ** 2, numbers))

#Proof
print(f"Numbers {numbers} have their respective squares {squares}.")