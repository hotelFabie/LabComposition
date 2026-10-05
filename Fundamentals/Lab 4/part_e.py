# Part E 

# -----1-----
def celsius_to_fahrenheit(celsius) -> float: 
    return celsius * 9/5 + 32

def classify_temperature(celsius) -> str:
    if celsius >= 30:
        return 'hot'
    elif celsius >= 10 and celsius < 30:
        return 'warm'
    else:
        return 'cold'

def format_temperature(celsius, fahrenheit, classification) -> str:
    return f"It is {classification} today,\nwith temperatures landing at {celsius} degrees celsius,\nor {fahrenheit} degrees fahrenheit."

def get_temperature_report(celsius ) -> str:
    fahrenheit = celsius_to_fahrenheit(celsius)
    classification = classify_temperature(celsius)
    return format_temperature(celsius, fahrenheit, classification)

print(get_temperature_report(25))

# -----2-----
def get_subtotal(price, amount : int) -> float:
    return price * amount

def get_discount(percentage) -> float:
    return 1 - (percentage / 100)

def get_total(subtotal, discount) -> float:
    return subtotal * discount

def calculate_small_order(number_of_items: int) -> float: 
    discount = get_discount(30)
    subtotal = get_subtotal(300, number_of_items)
    return get_total(subtotal, discount)

# -----3-----
#The closest thing I could find is question 2 from Part C - calculate_price(price, quantity=1, discount=0),
#and it is already quite similar to what we have done right above here, but as the goal here is decomposition,
#it should be fine. :-)

def calculate_discount(percentage):
    return 1 - (percentage / 100)

def calculate_quantified_price(quantity, price):
    return quantity * price

def actual_price(quantified_price, discount):
    return quantified_price * discount

def calculate_price(price, quantity=1, discount_percentage=0) :
    discount = calculate_discount(discount_percentage)
    quantified = calculate_quantified_price(quantity, price)
    new_price = actual_price(quantified * discount)
    return new_price

# -----4-----
def like_main() -> None:
    get_temperature_report(25)
    calculate_small_order(5)
    calculate_price(300)