#Part F

# -----1-----
products = [
    {"name" : "  Tennis bAll  ", "category" : "ball", "price" : 1.99, "stock": 130},
    {"name" : "badMINton bALl ", "category" : "ball", "price" : 1.99, "stock": 80},
    {"name" : "BaskeTbaLl              ", "category" : "ball", "price" : 6.99, "stock": 40},
    {"name" : "  foOTball", "category" : "ball", "price" : 4.99, "stock": 120},
    {"name" : "    kETTLEbell    ", "category" : "gym", "price" : 8.99, "stock": 0},
    {"name" : "tREADmill ", "category" : "gym", "price" : 259.99, "stock": 0},
    {"name" : "  skipPING roPE   ", "category" : "miscellaneous", "price" : 9.99, "stock": 15},
    {"name" : " hanD griP ", "category" : "miscellaneous", "price" : 3.99, "stock": 0},
    {"name" : "SwIm ShOrtS", "category" : "swimwear", "price" : 19.99, "stock": 0},
    {"name" : "          CompeTiTiOn SwimSuIt", "category" : "swimwear", "price" : 39.99, "stock": 4},
    {"name" : "5Kg weIGHT  ", "category" : "gym", "price" : 3.99, "stock": 20},
    {"name" : " 10kG WEight    ", "category" : "gym", "price" : 7.99, "stock": 0},
]

#Proof
print(products)

# -----2-----
cleaned_products = [
    {"name" : product["name"].strip().lower(), 
     "category" : product["category"], 
     "price": product["price"], ""
     "stock" : product["stock"]} 
     for product in products]

#Proof
print(cleaned_products)

# -----3-----
in_stock_products = [product for product in cleaned_products if product["stock"] > 0]

#Proof
print(in_stock_products)

# -----4-----
categories = {product["category"].strip().lower() for product in cleaned_products}

#Proof
print(categories)

# -----5-----
product_values = {product["name"] : (product["price"] * product["stock"]) for product in cleaned_products}

#Proof
print(product_values)

# -----6-----
descending_value_products = sorted(cleaned_products, key=lambda product: product["price"] * product["stock"], reverse = True)

#Proof
print(descending_value_products)

# -----7-----
#Considered we already have the ordering, we just print everything.
print("MOST TO LEAST ACCUMULATED VALUE (CURRENTLY)")
for rank, product in enumerate(descending_value_products, start=1):
    print(f"{rank}. {product['name']} ({product['category']}) | stock: {product['stock']}, price: {product['price']}")
    
# -----8-----
#Combining them related to this assignment.
name = ["multi-purpose room speaker", "hockey puck"]
category = ["miscellaneous", "ball"]
stock = [3, 30]
price = [459.99, 7.99]

additional_products = [
    {"name" : n, "category" : c, "stock" : s, "price" : p} 
    for n, c, s, p in zip(name, category, stock, price)
]

#Proof
for product in additional_products:
    print(product)

# -----9-----
shapes = [
    {"name" : "triangle", "corners" : 3, "weight" : 38},
    {"name" : "square", "corners" : 4, "weight" : 40},
    {"name" : "pentagon", "corners" : 5, "weight" : 53},
    {"name" : "hexagon", "corners" : 6, "weight" : 60},
    {"name" : "heptagon", "corners" : 7, "weight" : 75},
    {"name" : "octagon", "corners" : 8, "weight" : 80},
    {"name" : "nonagon", "corners" : 9, "weight" : 90},
    {"name" : "decagon", "corners" : 10, "weight" : 102},
]

over_complicated = [{"name" : shape["name"], "corners" : shape["corners"], "weight" : shape["weight"]} for shape in shapes if shape["corners"] > 0 and shape["weight"] != 0 and len(shape["name"]) > -1+1 and shape["weight"] % shape["corners"] == 0 and int(str(shape["weight"])[0]) == shape["corners"]]

clear = [
    shape 
    for shape in shapes
    if shape["weight"] > 0
    and shape["weight"] % shape["corners"] == 0 
]

#Proof (Comparison to see that they give the same result)
print(over_complicated)
print(clear)

#The clear one does not need extract information it already can get quickly, 
#and does not have too many unnecessary invalidation checks, with the checks being in a clear order.
#Furthermore, breaking it down into several lines makes it more readable.