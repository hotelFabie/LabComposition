# Part E
# -----1-----
count = 10
while count >= 0:
    print(count)
    count -= 1

# -----2-----
password = "secret"

attempt = str(input("enter password: "))

while attempt != password:
    attempt = str(input("wrong, try again: "))

print("welcome in!")

# -----3-----
menu = "-hello, you can do the following- \nbuy - sell - ask - investigate - quit"
normal_action = ("buy", "sell", "ask", "investigate")

print(menu)
option = str(input(">"))
while option != "quit":
    if option not in normal_action:
        print("you tried an unknown action")
    else:
        print(f"you did the action: {option}")
    print(menu)
    option = str(input(">"))
print("quitting")

# -----4-----
total = 0

number = int(input("give a number: "))

while number != 0:
    total += number
    number = int(input("give a number: "))

print(f"total: {total}")

# -----5-----
secret_number = 23

guess = int(input("guess the secret number: "))
while guess != secret_number:
    if guess < secret_number:
        print("the number is higher")
    elif guess > secret_number:
        print("the number is lower")
    guess = int(input("guess the secret number: "))

print(f"you got it! it was {secret_number}")