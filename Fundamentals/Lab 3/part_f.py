# Part F
# -----1-----
for i in range (1, 101):
    if i % 7 == 0 and i % 9 == 0:
        print(f"it was {i}")
        break
        
# -----2-----
strings = ["", "hey", "hola", "hej", "", "konnichiwa", ""]

for string in strings:
    if not string:
        continue 
    else:
        print(string)

# -----3-----
names = ["joseph", "rayan", "filip", "emilie", "jason"]

found = False

for name in names:
    if name == "jz":
        found = True
        print("found")
        break

if not found:
    print("the value was never found, as the found variable was never set to 'True'") 
    
# -----4-----
numeric_values = [-2, 12, 85, -99, 999, 50, 250]

for value in numeric_values: 
    if value < 0:
        continue
    elif value == 999:
        print("STOP!!!")
        break
    print(value)