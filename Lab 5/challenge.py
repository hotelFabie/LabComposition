#Lab 5 Challenge

#:::Part 1
products = [
    {"name" : "NES", "price" : "", "category" : "Game Console"},
    {"name" : "Switch Controller", "price" : "", "category" : "Controller"},
    {"name" : "Playstation 5", "price" : "", "category" : "Game Console"},
    {"name" : "Classic Famicom Controller (JP)", "price" : "", "category" : "Controller"},
    {"name" : "Switch 2", "price" : "", "category" : "Game Console"},
    {"name" : "Nintendo 3DS Case (Pink)", "price" : "", "category" : "Case"},
    {"name" : "Nintendo DS Case (Super Mario 64 DS Edition)", "price" : "", "category" : "Case"},
    {"name" : "Steam Deck", "price" : "", "category" : "Game Console"}
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
print(make_order(customers[0]["id"], customers[0]["name"], products[1], products[4], shipping_method="DHL", discount=10))

#:::Part 3
def calculate_subtotal():
    return ()

#:::Part 4


#:::Part 5


#:::Part 6


#:::Part 7


#:::Part 8

