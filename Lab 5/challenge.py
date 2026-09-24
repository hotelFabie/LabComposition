#Lab 5 Challenge

#:::Part 1
products = [
    {"name" : "NES", "price" : 179.99, "category" : "Game Console"},
    {"name" : "Switch Controller", "price" : 79.99, "category" : "Controller"},
    {"name" : "Playstation 5", "price" : 499.99, "category" : "Game Console"},
    {"name" : "Classic Famicom Controller (JP)", "price" : 29.99, "category" : "Controller"},
    {"name" : "Switch 2", "price" : 579.99, "category" : "Game Console"},
    {"name" : "Nintendo 3DS Case (Pink)", "price" : 19.99, "category" : "Case"},
    {"name" : "Nintendo DS Case (Super Mario 64 DS Edition)", "price" : 19.99, "category" : "Case"},
    {"name" : "Steam Deck", "price" : 1199.99, "category" : "Game Console"}
]

customers = [
    {"name" : "Oin Dori", "email" : "mugen@yahoo.jp", "id" : 1},
    {"name" : "Hemlis", "email" : "secrecy@protonmail.com", "id" : 2},
    {"name" : "No No Mal", "email" : "ordinary@gmail.com", "id" : 3},
    {"name" : "Box Shadow", "email" : "shadow.box@mailbox.org", "id" : 4},
    {"name" : "Suverän", "email" : "sovereign@soverin.net", "id" : 5},
]

#:::Part 2
def make_order(id : int, customer_name : str, *products, **optionals) -> dict:
    #gotta test this first...
    if not products:
        return None
    
    order = {"id" : id, "customer" : customer_name, "products" : []}
    for product in products:
        order['products'].append(product)

    if optionals:
        order["optionals"] = {}
        for option_name, value in optionals.items():
            order["optionals"][option_name] = value

    return order

#Testing a failing one first
print(make_order(customers[0]["id"], customers[0]["name"]))

#Testing an extensive one
print(make_order(customers[0]["id"], customers[0]["name"], products[1], products[4], company="DHL", discount=10))

order_one = make_order(customers[0]["id"], customers[0]["name"], products[7], discount=20, priority=True, message="Fun is Key.")
order_two = make_order(customers[1]["id"], customers[1]["name"], products[6], products[5])
order_three = make_order(customers[2]["id"], customers[2]["name"], products[4], company="DB Schenker", shipping="rapid express")
order_four = make_order(customers[3]["id"], customers[3]["name"], products[0])
order_five = make_order(customers[4]["id"], customers[4]["name"], )
#these last three should definitely have some optional things...
#expensive one with shipping is 尤も.

#:::Part 3
def calculate_subtotal(*prices : int | float) -> int | float | None:
    if not prices:
        return None
    
    subtotal = 0
    for price in prices:
        subtotal += price 
    return subtotal

#Test
print(calculate_subtotal(59, 139, 79, 199))

#:::Part 4
#*just assuming right a dictionary is what we'll return, though i'm not sure yet...*
def configure_order(**optionals) -> dict: 
    if not optionals:
        return None
    configuration = {}
    for optional, value in optionals.items():
        configuration[optional] = value
    return configuration

#Test
print(configure_order(company="DB Schenker", discount=10))

#:::Part 5
#"... information already exists in collections", so it just happens to be here, I guess?

#ONLY ONE IS DONE SO FAR.

prices_one = [79, 99, 159, 199]

#Positional unpacking 1 and 2
print(calculate_subtotal(*prices_one))


#Dict 1
settings_one = {
    "" : "", 
    "" : ""
}

#Dict 2
settings_two = {
    "campaign_code" : "Q5WT8",
    "company" : "PostNord",
    "discount" : 15,
    "message" : "",
    "priority" : True,
    "shipping" : "express"
}

#ONLY TWO IS DONE SO FAR.

#Dictionary unpacking 1 and 2
print(configure_order(**settings_two))

#:::Part 6

#WIP

def produce_summary(id : int, customer : str, *messages, **metadata) -> str:
    summary = f"id: {id}, customer name: {customer}" 
    
    if messages:
        summary += "messages: "
        for message in message:
            summary += message
        
    if metadata:
        summary += "metadata: "
        for key, value in metadata.items():
            summary += (f"[{key}: {value}]")
    return summary

#Test - JUST TESTING THAT IT WORX FIRST B4 PUTTING IN ACTUAL DATA.
print(produce_summary(6, "jason", "bleep", "bloop", thing="thing", moop="meep"))

#:::Part 7


#:::Part 8

