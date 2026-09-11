# Part H
# -----1-----
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: 
        #Just to make it more visible that all values are iterated through
        print(".")
        
# -----2-----
sentence = "Hello, my name is Fabian Vikman."
vowel = ["a", "i", "u", "e", "o", "y"]
count = 0

for letter in sentence:
    if letter in vowel:
        count += 1

print(f"count is: {count}")

# -----3-----
value_list = ["kaze", "hiroi", "dengon", "kaze", "mirai", "yuugen", "kaze", "yuugen", "hiroi", "roudou", "genshou", "mirai", "mirai"]
seen = []
duplicates = []

for value in value_list:
    if value in seen:
        duplicates.append(value)
    seen.append(value)

print(duplicates)

# -----4-----
numbers = [3, 5, 2]

for number in numbers:
    row = number * "*"
    print(row)