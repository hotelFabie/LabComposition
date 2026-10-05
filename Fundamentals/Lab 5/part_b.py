#Part B

# -----1-----
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number

    return total

#Proof for self
print(add_all(1, 2, 3, 4, 5))

# -----2-----
def average(*numbers):
    if len(numbers) == 0:
        return "requires at least one value to count an average"
    else:
        total = 0
        for number in numbers:
            total += number

        average = total / len(numbers)
        return average

print(average())
print(average(3, 4, 5))
        


# -----3-----
def longest_word(*words):
    longest_word = ""
    for word in words:   
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

print(longest_word("Volvo", "Mercedes Benz", "Ferrari", "Chrysler"))

# -----4-----
#We don't want a separator at the end, as it does not separate from anything, hence the if-else condition inside.
def build_sentence(separator, *words):
    sentence = ""
    for word in words:
        if word != words[-1]:
            sentence += f"{word}{separator}"
        else:
            sentence += word

    return sentence

print(build_sentence(",", "john", "is", "very", "happy"))

# -----5-----
def describe_scores(student_name, *scores):
    total = 0
    number_of_scores = 0
    for score in scores:
        number_of_scores += 1
        total += score

    average = total / len(scores)

    #Not specified what format was expected here, so I chose a dictionary.
    return {"name" : student_name, "number_of_scores" : number_of_scores, "average score" : average}

print(describe_scores("Jason", 80, 70, 90))