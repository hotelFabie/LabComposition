# Part E
# -----1 & 2-----
first_name = str(input("First name: ")).strip()
last_name = str(input("Last name: ")).strip()
city = str(input("City: ")).strip()
year_of_birth = str(input("Year of birth: ")).strip()
favorite_language = str(input("Favorite programming language: ")).strip()

# -----3-----
user_id = first_name[0] + last_name[:3] + year_of_birth[2:] 

# -----4-----
print(f"Name: {first_name} {last_name}, with user id [{user_id}]")
print(f"Details: Born {year_of_birth}, living in {city}, likes {favorite_language}")

# -----5-----
print(f"{first_name[0]}.{last_name[0]}., {len(first_name) + len(last_name)}, {favorite_language[::-1]}")

# -----6----- 
height = float(input("Height (in m): "))
is_married = bool(input("Married (1 = Yes, 0 = No): "))
nationality = str(input("Which country do you come from?: "))
print("--Some extra information about this person--")
print(f"They are {height}m tall, it is {is_married} that they are married, and they come from {nationality}")