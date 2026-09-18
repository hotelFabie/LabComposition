# Part A

# -----1-----
def greet() -> None:
    print("Hello!")

course = {"name" : "A Fun Course", "hours" : 45}

def show_course_name() -> None:
    print(course["name"])

def print_separator() -> None:
    print("----------")

# -----2-----
def greet_person(name) -> None:
    print(f"Hello, {name}")

def introduce(name, city) -> None:
    print(f"{name} is from {city}")

# -----3-----
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

# -----4-----
#Parameters are the variables/values specified in the function definition, describing what is needed for the function to be used.
#Arguments are the basically the actual values you insert into the function call, sort of like a response to the parameters.

#Here we have the parameters in the parenthesis.
def divide(a,b):
    return a / b

#And here are the arguments, basically replacing every "a" inside the function with what is the inserted first argument.
division_result = divide(6, 2)

# -----5-----
def calculate_area(width, height):
    return width * height

def calculate_space(width, height, length):
    area = calculate_area(width, height)
    return area * length

space = calculate_space(3, 4, 5)