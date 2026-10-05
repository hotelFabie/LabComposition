# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5}
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.

# Solution:
total_value = 0
highest_priced_product = products[0]

for product in products:

    #Name of everything that is in stock.
    if product["stock"] > 0:
        print(product["name"])

        #Calculating the total value.
        total_value += (product["price"] * product["stock"])

        #Maximum price comparison.
        if product["price"] > highest_priced_product["price"]:
            highest_priced_product = product

#Printing the total value.
print(f"The total value is: {total_value}")

#Printing in-stock product with the highest price.
print(f"Highest price product is: {highest_priced_product['name']}")
        
# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.

# Solution:
def calculate_average(scores : list) -> int | float:
    total = 0

    for score in scores:
        total += score

    average = total / len(scores)

    return average

def create_result(scores : list) -> str:
    if calculate_average(scores) >= 70:
        return "PASS"
    return "FAIL"

print(f"The average score is: {calculate_average(scores)}")
print(f"The final result is: {create_result(scores)}")

# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {
    "discount": 10,
    "shipping": 49,
    "priority": True
}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.

# Solution:
def calculate_order(customer, *prices, **settings):
    sub_total = 0
    for price in prices:
        sub_total += price

    #To create the final total value, we'll need the value of the subtotal first to apply additional calculations.
    final_total = sub_total
    
    #Adding discount and shipping
    for setting, setting_value in settings.items():
        if setting == "discount":
            final_total *= (1 - (setting_value / 100))

        if setting == "shipping":
            final_total += setting_value

    return {"customer" : customer, "subtotal" : sub_total, "final_total" : final_total, "settings" : settings}

#Call and print.
result = calculate_order("Anna", *product_prices, **order_settings)
print(result)

# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False}
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.

# Solution:
# 1:
normalized_players = [
    {"name" : player["name"].strip().title(), 
     "score" : player["score"], 
     "active" : player["active"]} 
    for player in players
]

# Proof
print(normalized_players)

# 2:
active_passing_players = [
    {"name" : player["name"], 
     "score" : player["score"], 
     "active" : player["active"]} 
    for player in normalized_players
    if player["active"] 
    and player["score"] >= 80
]

# Proof
print(active_passing_players)

# 3:
descending_players = sorted(normalized_players, key = lambda player : player["score"], reverse=True)

# Proof 
print(descending_players)

# 4:
for rank, player in enumerate(descending_players, start = 1):
    print(f"{rank}. {player['name']} - {player['score']}")

# 5:
player_names = ["Anna", "David", "Sara", "Leo", "Emma", "Oscar"]
player_scores = [85, 72, 94, 67, 88, 76]

assembled_players = [{"name" : n, "score" : s} for n, s in zip(player_names, player_scores)]

for player in assembled_players:
    print(f"{player['name']} - {player['score']}")