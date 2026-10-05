# Part C
# -----1-----
sentence = "   wHoaH, seTTLE dOwN buDDY    "
print(f"Length: {len(sentence)}")
print(f"Lowercase version: {sentence.lower()}")
print(f"Uppercase version: {sentence.upper()}")
print(f"Whitespace removed: {sentence.strip()}")

# -----2-----
first_name = str(input("Enter your first name: "))
last_name = str(input("Enter your last name: "))
print(f"Your full name is {first_name} {last_name}")

# -----3-----
string = 'python programming'

#First character
print(string[0])

#Last character
print(string[-1])

#First six characters
print(string[:6])

#Last eleven character
print(string[-11:])

#Reversed
print(string[::-1])
# -----4----- : Username Generator
first_name = str(input("Enter your first name: ")).strip().lower()
last_name = str(input("Enter your last name: ")).strip().lower()
username = first_name[:3] + last_name[:5]
print(f"Generated username: [{username}]")

# -----5-----
email = str(input("Give an email address: "))

parts_of_email = email.split("@")

print(f"The part before the @ is {parts_of_email[0]}, and the one after is {parts_of_email[1]}")

# -----6-----
sentence = "Java"
replace_sentence = sentence.replace("Java", "Python")
print(f"Sentence before: {sentence}, sentence after: {replace_sentence}")
