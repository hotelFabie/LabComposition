# Part B 

# -----1-----
def is_even(number) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False

# -----2-----
def get_larger(a, b) -> int | float:
    if a > b:
        return a
    else:
        #This else accounts for when they are equally big as well, because if not >, then <=
        return b
        
# -----3-----
def classify_score(score : int) -> str:
    if score >= 80:
        return "PASS"
    else:
        return "FAIL"

# -----4-----
def full_name(first_name : str, last_name : str) -> str:
    print(f"{first_name, last_name}")

# -----5-----
def calculate_discount(price, percent) -> float:
    return price - price * (percent / 100)

# -----6-----
def print_word(word):
    print(word)

def return_word(word):
    return word

var_one = print_word("yoru")

var_two = return_word("yoru")

print(type(var_one))
print(type(var_two))

#In the first case, we simply just print to the console, but we can't really store the result of just a normal print in a variable.
#So when checking the type, we'll see that the second variable is the only actually having a value stored (type str, vs. NoneType).
#return does not automatically write to the terminal by itself.