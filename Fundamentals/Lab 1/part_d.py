# Part D
# -----1-----
string_construction = "Everglades"

print(f"1> output should be: 'es', is: {string_construction[-2:]}")
print(f"2> output should be: 'glades', is: {string_construction[4:]}")
print(f"3> output should be: 'r', is: {string_construction[3]}")
print(f"4> output should be: 'l, is: {string_construction[-5]}")
print(f"5> output should be: 'vls', is: {string_construction[1::4]}")
print(f"6> output should be: 'glad', is: {string_construction[4:-2]}")
print(f"7> output should be: 'el, is: {string_construction[2:-2:3]}")
print(f"8> output should be: 'Eegae', is: {string_construction[::2]}")

# -----2-----
text_to_slice = "Artificial Intelligence"
#1: Artificial
slice_one = text_to_slice[0:10]
print(slice_one)

#2:Intelligence
slice_two = text_to_slice[11:]
print(slice_two)

#3: Space between the two words
slice_three = text_to_slice[10:11]
print(slice_three)

#4: Backwards Intelligence
slice_four = text_to_slice[-1:-14:-1]
print(slice_four)

#5: Backwards Artificial
slice_five = text_to_slice[-14::-1]
print(slice_five)

#6: Entirety reversed
slice_six = text_to_slice[::-1]
print(slice_six)

# -----3-----
#Split: You want to store each value from an ingredient list somewhere, so you break it down first by removing
#unnecessary information to organize it.
ingredient_list = "shallots, garlic, onion, potatoes"
ingredients = ingredient_list.split(",")
print(f"{ingredients}")

#A person fills out information for attending an event, but accidently didn't catch he made a space at the end
entered_name = "Blake  "
adjusted_name = entered_name.strip()
print(f"{adjusted_name}")

#Replace: If you want to provide info about something new, but slightly similar, we can base it off of something
#that already exists.
juice = "Orange Juice"
new_juice = juice.replace("Orange", "Apple")
print(f"{new_juice}")

#Check if a person from the staff is attending an event based on the text:
staff = "Abdul, Keitaro, Lukas, Yasmine"
is_keitaro_present = "Keitaro" in staff
print(f"It is {is_keitaro_present} that Keitaro will be there.")

# -----4----- : String Immutability
modify_this_string = "Hapan"
#modify_this_string[0] = "J" <-- Modifying directly won't work, because it is immutable.

new_string = "J" + modify_this_string[1:]
print(new_string)
#This works, because we're taking a part of something immutable ("take", not "attempt to change") 
#to create a new, not-touched-upon variable.