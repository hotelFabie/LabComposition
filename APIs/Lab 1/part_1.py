import base_functionality as bf

#1
products_one = bf.get_json("https://fakestoreapi.com/products/")

sorted_one = sorted(products_one, key = lambda product : product['price'])

for product in sorted_one:
    print(f"{product['title']} - {product['price']}") 

#2


#3

#4

#5