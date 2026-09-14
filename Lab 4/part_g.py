# Part G

# -----1-----
example_list = [1, 5, 8, 3, 9, 4, 7]

def max_and_min(list):
    #Yet again, gotta start somewhere to have an actual legit value to compare to.
    max = list[0]
    min = list[0]

    for item in list:
        if item > max:
            max = item
        if item < min:
            min = item

    return max, min

#Proof for myself
print(max_and_min(example_list))

# -----2-----
def is_palindrome(word : str) -> bool:
    for i in range(len(word) // 2):
        if word[i] != word[-i-1]:
            return False

    return True

#Proof for myself
print(is_palindrome("melakalem"))

# -----3-----
def dictionarize_word(word : str):
    dictionary = dict()
    for character in word:
        if character in dictionary:
            value = dictionary[character] + 1
            dictionary.update({character : value})
        else:
            dictionary.update({character : 1})

    return dictionary

print(dictionarize_word("accommodation"))


# -----4-----
different_values = [-5, 3, -2, 0, 8, -4, -7, 2]

def assign_values(values : list):
    pnz_dict = dict()

    for value in values:
        if value > 0:
            value_meaning = 'positive'
        elif value < 0:
            value_meaning = 'negative'
        else:
            value_meaning = 'zero'

        if value_meaning in pnz_dict:
            count = pnz_dict[value_meaning] + 1
            pnz_dict.update({value_meaning : count})
        else:
            pnz_dict.update({value_meaning : 1})

    return pnz_dict

#Proof for myself
print(assign_values(different_values))

# -----5-----
#I didn't realize it was not expected to not be done beforehand, so I'll just implement like I have before.
def add(a : int, b : int) -> int:
    """Returns the result of two integer arguments."""
    return a + b

def is_adult(age) -> bool:
    """Returns True if the person is 18 or older, otherwise False."""
    if age >= 18:
        return True
    else: 
        return False

def biggest_number(a: int, b: int, c: int) -> int:
    """Returns the biggest of three numbers."""
    biggest_number = 0
    if a > b:
        biggest_number = a
    else: 
        biggest_number = b

    if c > biggest_number:
        biggest_number = c

    return biggest_number

def count_elements(elements: list) -> int:
    """Returns the amount of numbers in a list."""
    count = 0
    for element in elements:
        count += 1

    return count

def half_or_double(value : int) -> int | float:
    """Returns half of the inserted value if it is under 1000, or double the inserted value if it is over 1000"""
    if value > 1000:
        return value * 2
    else: 
        return value / 2