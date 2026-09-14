# Part 4

#-----1-----
def calculate_total(numbers) -> float | int:
    total = 0
    for number in numbers:
        total += number

    return total

#-----2-----
def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1

    return count

#-----3-----
def get_long_words(words, minimum_length):
    long_words = []
    for word in words:
        if len(word) >= minimum_length:
            long_words.append(word)

    return long_words

#-----4-----

students = [
    {"name" : "James", "age" : 27},
    {"name" : "Melissa", "age" : 29},
    {"name" : "Nancy", "age" : 40}
]

def find_student(students, name):
    for student in students:
        if student["name"] == name:
            return student

    return None

print(find_student(students, "Melissa"))
print(find_student(students, "Aubrey"))

#-----5-----

graded_students = [
    {"name" : "Hogan", "score" : 57},
    {"name" : "Caramel", "score" : 93},
    {"name" : "Mason", "score" : 87}
]


def average_score(students) -> int | float:
    accumulated_score = 0
    for student in students:
        accumulated_score += student['score']

    return accumulated_score / len(students)

print(average_score(graded_students))

#-----6-----

users = [
    {"username" : "enterprise78", "active" : True},
    {"username" : "jamradio39", "active" : False},
    {"username" : "21compass", "active" : True}
]

def get_active_users(users):
    active_users = []
    for user in users:
        if user["active"]:
            active_users.append(user)

    return active_users

print(get_active_users(users))