from pprint import pprint

from datetime import datetime
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["webshop"]

# #Exercise 1
# res_one = db.products.find({"category" : "Accessories"})
# for product in res_one:
#     print(product.get("name"))
# #4 results retrieved.

# #Exercise 2
# res_two = db.customers.find({"city" : "Göteborg"})
# for customer in res_two:
#     print(f"{customer.get('first_name')}, {customer.get('last_name')}")
# #2 results retrieved.

# #Exercise 3
# res_three = db.products.find()
# for product in res_three:
#     print(f"{product.get('name')}, {product.get('price')}")
# #12 results retrieved.

# #Exercise 4
# res_four = db.customers.count_documents({'city' : 'Uppsala'})
# print(f"Customers in Uppsala: {res_four}")
# #Result shows a count of 3, which was expected.

# #Exercise 5
# res_five = db.products.find_one({'name' : 'Sandals'})
# print(f"Stock: {res_five.get('stock')}")
# #Result shows 22, which was expected.

#Exercise 6
res_six = db.customers.find({"newsletter" : True})

for customer in res_six:
    print(customer.get('first_name'))
#Retrieved 3 results: Anna, Sara, Oskar.

#Exercise 7
res_seven = db.customers.insert_one({"first_name" : "Fabian", "last_name" : "V.", "email" : "fabianv@fabianworld.tv", "city" : "TV City", "joined" : datetime(2026, 10, 13), "phone" : "012-1212121"})

print(f"Inserted id: {res_seven.inserted_id}")

me = db.customers.find_one({'email': 'fabianv@fabianworld.tv'})
pprint(me)

#Exercise 8
# products_eight = [
#     {"_id": 13, "name": "Air Force 1", "category": "Shoes", "price": 139, "stock": 3, "tags": ["limited"], "details": {"color" : "black", "shoelaces" : "camouflage noir"}},
#     {"_id": 14, "name": "Bape x Baby Milo Collaboration T-Shirt", "category": "Clothing", "price": 159, "stock": 30, "tags" : ["limited"], "details": {"color": "white", "material": "eco cotton"}}
# ]

# db.products.insert_many(products_eight)

# res_eight = db.products.count_documents({})
# print(f"Amount of products after insertion: {res_eight}")
# #Result shows 14, which was expected.

#Exercise 9
#using dict.get()

#Exercise 10
