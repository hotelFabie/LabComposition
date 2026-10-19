import api_client as ac
import requests

# #1
# products_1 = ac.get_json("https://fakestoreapi.com/products/")

# sorted_1 = sorted(products_1, key = lambda product : product['price'])

# for product in sorted_1:
#     print(f"{product['title']} - {product['price']}") 

# #2
# products_2 = ac.get_json("https://fakestoreapi.com/products/")

# for product in products_2:
#     print(f"{product['title']} - {product['category']}") 

# category = input("give a category> ").strip()
# products_2_specific = ac.get_json(f"https://fakestoreapi.com/products/category/{category}")
# print(f"items in the {category} category: {len(products_2_specific)}")


# #Probably need to fix here so that it gives the correct error.
# if products_2_specific:
#     products_2_specific_sorted = sorted(products_2_specific, key = lambda product: product['price'])
#     print(f"the cheapest is: {products_2_specific_sorted[0]['title']} - {products_2_specific_sorted[0]['price']}")

# #3
# #Was already done since the start.

#4
product_4 = {
    "title" : "FabieBoard",
    "price": 999.9,
    "description": "An electronic device with hidden potential",
    "image": "https://fabieworld.org/pictures/fabieboard.png",
    "category" : "electronics"
}

response_4_post = requests.post("http://fakestoreapi.com/products", json=product_4)
print(response_4_post.status_code)
print(response_4_post.json())

response_4_patch = requests.patch("https://fakestoreapi.com/products/7", json={'price' : 1000})

print(response_4_patch.json())
print(response_4_patch.status_code)

#5