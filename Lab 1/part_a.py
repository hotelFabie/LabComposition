# Part A
# -----1-----
print("Fabian Vikman")
print("Python and AI - System developer")
print("Today's study goal is to get comfortable with the basics of Python.")

# -----2-----
person = "Kalle Kula"
age = 25
height = 1.90
is_student = True

print(f"Person: {person}, type: {type(person)}")
print(f"Age: {age}, type: {type(age)}")
print(f"Height: {height}m, type:{type(height)}")
print(f"Is a student: {is_student}, type: {type(is_student)}")

# -----3-----
binary_value = 1

print(f"Type (before) is: {binary_value}")

binary_value = bool(binary_value)

print(f"Type (after) is: {binary_value}")

#The code above demonstrates how variables in Python do not have to be bound to a specific data type, 
#and can in some cases be converted to another type (of course, depending on what value it is).

# -----4-----
number_one = 9
number_two = 2

#Addition
print(f"Addition between {number_one} and {number_two} gives: {number_one + number_two}")

#Subtraction
print(f"Subtraction between {number_one} and {number_two} gives: {number_one - number_two}")

#Multiplication
print(f"Multiplication of {number_one} and {number_two} gives: {number_one * number_two}")

#Division
print(f"Division of {number_one} by {number_two} gives: {number_one / number_two}")

#Floor division
print(f"Floor division of {number_one} by {number_two} gives: {number_one // number_two}")

#Remainder
print(f"Remainder of {number_one} by {number_two} gives: {number_one % number_two}")

#Exponentiation
print(f"Exponentiation of {number_one} to the power of {number_two} gives: {number_one ** number_two}")

# -----5-----
number = "5"
number = int(number)
number -= 2
print(number)

originally_integer = 10
originally_integer = float(originally_integer)

print(f"Result with decimals considered is {originally_integer}")

#Number to string: Concatenating numbers to a string without an f-print
age = 30
age = str(age)
print("This guy is " + age + " years old.")