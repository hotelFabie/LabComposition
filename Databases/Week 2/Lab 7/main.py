from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

#Exercise 1
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
# res_three = db.customers.find({"city" : {"$in" : ["Stockholm", "Malmö"]}})
# for customer in res_three:
#     print(f"({customer.get('_id')}) {customer.get('first_name')} {customer.get('last_name')}")
# #3 rows retrieved.

#Exercise 4
# res_four = db.products.find({"details.color" : "white"})
# for product in res_four:
#     print(product.get('name'))
# #3 rows retrieved.

#Exercise 5
# res_five = db.products.find({"tags" : "sport"})
# for product in res_five:
#     print(f"{product.get('name')}, tags: {product.get('tags')}")
# #3 rows retrieved.

#Exercise 6
# res_six = db.products.find().sort("price", 1).limit(5)
# for product in res_six:
#     print(f"{product.get('name')} - {product.get('price')}")
# #5 rows retrieved.

#Exercise 7


#Exercise 8


#Exercise 9


#Exercise 10

