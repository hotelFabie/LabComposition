#Part F

# -----1-----
#i have to distort these a little bit

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
#use zip to combine at least one pair of separate derived lists in a meaningful way.
#we could make four lists, and then add it to this thing.
name = []
category = []
stock = []
price = []

# -----9-----

