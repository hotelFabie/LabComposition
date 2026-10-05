#Part G

# -----1-----
def merge_settings(defaults, **overrides):
    #Don't want to change what we pass as argument by reference.
    merged = defaults.copy()

    for key, value in overrides.items():
        merged[key] = value
        
    return merged

#Proof for myself.
default = {"alpha" : 38, "charlie" : 56, "echo" : 74}
print(merge_settings(default, bravo=47, delta=65))

# -----2-----
def call_summary(function_name, *args, **kwargs):
    call = f"{function_name}("

    for arg in args:
        if arg != args[0]:
            call += f", {arg}"
        else:
            call += f"{arg}"

    for key, value in kwargs.items():
        call += f", {key}={value}"

    call += ")"

    return call

#Proof for myself.
print(call_summary("deteriorate", "health", "mind", endurance=0.65, physical_strength=0.5))

# -----3-----
def num_statistics(*numbers):
    count = 0
    total = 0
    average = 0
    min_ = numbers[0]
    max_ = numbers[0]
    for number in numbers: 
        count += 1
        total += number
        if number > max_:
            min_ = number
        if number < min_:
            max_ = number

    average = total / len(numbers)

    return {"count" : count, "total" : total, "average" : average, "min" : min_, "max" : max_}

#Proof for myself.
print(num_statistics(3, 5, 7, 9, 11, 13, 15))

# -----4-----
#[1] What will be returned on the last line?
def total(a, b):
    total += a
    total += b
    return total
    
total += 1

#Assuming nothing, because the local variable 'total' will die out, and so we're not adding onto anything.

#And it was correct! :D 

#[2]
result = 0

def exponentiate(x, y):
    global result
    result += x ** y
    return result
    
result += 0.0001

#Assuming we'll get the exponentiation with 0.0001 added, because it is a global variable now.
print(exponentiate(2, 4))

#And it worked! :D

#[3]
def jammy_radio():
    sound = "beeeep. x)"
    
    def make_noise():
        return sound

    return make_noise()

#What will the function return?
print(jammy_radio())

#I assume the sound: 'beeeep. x)'

#[4]
def inform():
    warning = "zzzzzzm"
    
    def megaphonize():
        warning = "ZWOOP! ZWOOP! ZWOOP!"

    megaphonize()
    print(warning)

#What will happen?
inform()

#The warning will never be changed, and it will only print out first warning.
#The internal variable will not be associated with anything.

#Correct! x)

#[5]
list = [1,2,3,4,5]

#Will this actually work?
new_list = list((1,2,3,4,5,6))
print(new_list)

#Most likely not, because we have "overwritten" a built-in word, so it will not work.

#Yeah, it was as expected.