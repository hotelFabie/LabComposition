# Part F
# -----1-----
seconds_total = int(input("Write the amount of time (in seconds): "))
hours = seconds_total // 3600
minutes = (seconds_total % 3600) // 60
seconds = seconds_total % 60

print(f"It is {hours} hours, {minutes} minutes, {seconds} seconds")

# -----2-----
number = int(input("Enter four digit number: "))

one = number // 1000 
two = (number - one*1000) // 100 
three = (number - one*1000 - two*100) // 10 
four = (number - one*1000 - two*100 - three*10)

print(f"one: {one}, two: {two}, three: {three}, four: {four}")

# -----3-----
text = "Fabian"
first = text[:2]
last = text[-2:] 
asterisks = "*" * (len(text) - 4)

print(first + asterisks + last)

# -----4-----
#(1) What will happen when we run this?
print(int(5.5)) #We will get 5, and the decimal values / fractions will be lost.

#(2) What will be the output of this?
funny_string = "JCahpianna"
print(funny_string[1::2]) #China

#(3) What will be the output of this?
weird_string = "a b  c  d e"
print(weird_string[1::2].strip()) #c

#(4) Will it become True or False?
negative_representation = "-1"
print(bool(negative_representation)) #True

#(5)What will be the output of this?
music = "do re mi fa so la ti do"
print(music[2::3]) #Just a bunch of spaces