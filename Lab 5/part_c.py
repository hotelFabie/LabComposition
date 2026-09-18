#Part C

# -----1-----
numbers = [10, 20, 30]

def get_3d_space(x, y, z):
    return x*y*z

#Proof for myself
print(get_3d_space(*numbers))

# -----2-----
person = ("John", "Guy", "New York")

def present_person(first_name, last_name, city):
    return f"This person is called {first_name} {last_name}, from {city}."

#Proof for myself
print(present_person(*person))

# -----3-----
#Length 3
first, *middle, last = [1, 2, 3]
print(first, middle, last)

#Length 5
first, *middle, last = [3, 4, 5, 6, 7]
print(first, middle, last)

#Length 8
first, *middle, last = [2, 3, 4, 5, 6, 7, 8, 9]
print(first, middle, last)

# -----4-----
#* in a function definition - e.g. "def add(*args)" means whatever you pass into this function will be turned into 
#an accumulated tuple, with which you choose internally what do do with each part this will be consisting of.

#* in a function call - e.g. "list = [1, 2, 3], add(*list)" in e.g. "add(a, b, c)" means to unpack the contents 
#to be filled in as arguments to the expected parameters, before the function does any executions.

#In that sense, a definition basically packs the arguments together, and a call deconstructs/unpacks it before doing anything.