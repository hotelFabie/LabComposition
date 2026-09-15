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
    return f"The function {function_name} is called, taking {args} as normal arguments, and {kwargs} as keyword arguments"

#Proof for myself.
call_summary("deteriorate()", )

#WIP: Gotta ask the teacher what this is even supposed to mean. 

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

