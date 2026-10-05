# Part B
# -----1-----
s1 = ""
s2 = " "
i1 = 0
i2 = 1
l1 = []
l2 = [" "]

if s1:
    print("1")
if s2:
    print("2")
if i1:
    print("3")
if i2:
    print("4")
if l2:
    print("5")
if l2:
    print("6")

# -----2-----
languages = ["japanese", "arabic", "mandarin", "english", "spanish"]

language = str(input("enter language: "))

if language in languages:
    print(f"{language} exists in the language list")
else:
    print(f"{language} does not exist in the language list")

# -----3-----
blocked = ["thre4t", "evilgoob", "letsbully"]

username = str(input("provide a username: "))

if username in blocked:
    print(f"{username} is blocked")
else:
    print(f"{username} is not blocked")
    
# -----4-----
people = {
    "Mason" : {"hungry" : False, "tall" : True},   
    "Ida" : {"hungry" : True, "tall" : False}
}

if not people["Mason"]["hungry"]:
    print("Mason is not hungry")

if people["Mason"]["tall"] and not people["Ida"]["tall"]:
    print("Mason is tall, and Ida is not.")