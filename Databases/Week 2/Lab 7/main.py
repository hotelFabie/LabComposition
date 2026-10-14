from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# #Exercise 1
# res_one = db.products.find({"price": {"$gt" : 1000}})
# for product in res_one:
#     print(f"{product.get('name')}, {product.get('price')}")
# #3 rows retrieved.

#Exercise 2
# res_two = db.orders.find({"status" : {"$ne" : "delivered"}})
# for order in res_two:
#     print(f"{order.get('_id')}, {order.get('status')}")
# #8 rows retrieved.

#Exercise 3
res_three = db.customers.find({"city" : {"$in" : ["Stockholm", "Malmö"]}})
for customer in res_three:
    print(f"({customer.get('_id')}) {customer.get('first_name')} {customer.get('last_name')}")
# 3 rows retrieved.

#Exercise 4


#Exercise 5


#Exercise 6


#Exercise 7


#Exercise 8


#Exercise 9


#Exercise 10

