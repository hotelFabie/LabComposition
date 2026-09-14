# Part C

#-----1-----
def greet(name, greeting='Hello') -> str:
    return f"{greeting}, {name}."

print(greet("Jacob"))
print(greet("Jake", "Wassup"))
print(greet(greeting="Hola", name="Joel"))

#-----2-----
#Assuming discount is between 0 and 1
def calculate_price(price, quantity=1, discount=0) -> int | float:
    adjusted_price = price * (1 - discount)
    return adjusted_price * quantity

#-----3-----
#Not sure how to specify a dict as a return type yet, so I skipped it.
def create_profile(name, city='Unknown', active=True):
    return {"name" : name, "city" : city, "active" : active}

#-----4-----
def build_space(x=1, y=1, z=1):
    return x*y*z

space = build_space(z=3, x=4, y=4)

print(f"The space is {space} units big.")

#-----5-----
#def faily_function(annoying_value=0, user_value):
#    return annoying_value + user_value

#The parameters that need arguments to be passed to the function in order for it to work needs to precede.
#Say a scenario where a function has with multiple variables, if every other had a preset value starting on the first one,
#it would make the insertion of values way harder for the Python interpreter to predict or do: "Should this parameter get that argument?", and so on. 