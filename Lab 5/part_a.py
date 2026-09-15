#Part A

# -----1-----
'''
course_name = "Python & AI"

def create_course():
    course_name = "C# & VR"
    return course_name

print(create_course())
print(course_name)

#When calling the function, it initializes a local variable with the same name, but different contents.
#As it is within a local scope, the print() will print what is seen locally. 
#The local scope basically only exists when the function is called, so when its execution has ended,
#course_name will now look at what the value is on the global scope.

# -----2-----
def counterize():
    counter = 0
    
counter += 1

#A yellow mark is visible within the IDE here under counter in the global context.
#The counter variable is actually defined within a local context, so it will not be visible everywhere; 
#it only exists within the timeframe of the function being called, so right now we're adding onto nothing, 
#a.k.a. we're not adding at all.

# -----3-----
global_number = 3

def increment():
    global_number += 1
    return global_number

print(increment())

#The local global_number is not associated with any external value, so it is as if we are adding onto something that is not
#defined yet. We need to pass something in to the function to change it.

def increment(number):
    number += 1
    return number 

global_number = increment(global_number)
print(global_number)
#Here we pass the value directly into the function and reassign it to the variable we took it from, and it works fine.
'''

# -----4-----
def outer_function():
    some_number = 3

    def inner_function():
        print(f"internal number is: {some_number}")

    inner_function()

outer_function()

# -----5-----
#list
items = [1, 2, 3]

#str
word = "Yo" 

#sum
total = 10

#max
def maximum(a : int, b : int):
    if a > b:
        return a
    else:
        #Accounts for them being of equal value too
        return b
    
