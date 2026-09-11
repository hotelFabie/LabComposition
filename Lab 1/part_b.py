# Part B
# -----1-----
current_year = 2026
name = str(input("What is your name?: "))
birth_year = int(input("What year were you born?: "))
print(f"{name}, your age is estimated to be: {current_year - birth_year}")

# -----2-----
item_price = float(input("What is the item price?: "))
discount_percentage = int(input("How big is the discount (in percentages)?: "))

#Make the percentage into something between 0 and 1, and multiply it to the price
final_price = round(item_price * (1 - (discount_percentage / 100)), 2)
print(f"The final price will be: {final_price}")

# -----3-----
celsius = float(input("Give degrees in celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} degrees celsius is {fahrenheit} degrees fahrenheit")

# -----4-----
length = float(input("Enter room length: "))
width = float(input("Enter room width: "))

area = length * width
perimeter = 2 * length + 2 * width
print(f"Area is: {area}, and perimeter is: {perimeter}")

# -----5----- : Based on the program right above this one
length = float(input("Enter room length: "))
width = float(input("Enter room width: "))

area = length * width
perimeter = 2 * length + 2 * width
print(f"Area is: {area}, and perimeter is: {perimeter}")

#If the user had entered 'hello', there would occur a TypeError, and it would not even continue to the calculations.