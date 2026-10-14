import datetime
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
# res_seven = db.orders.find({"items.product_id" : 2})
# for order in res_seven: 
#     print(f"Order {order.get('_id')}")
# #4 rows retrieved.

#Exercise 8
#Doing a check before the update to see what we will alter, instead of blindly committing an unreversible action.
# res_eight = db.products.find({'category' : 'Accessories'})
# for product in res_eight:
#      print(f"{product.get('name')} - {product.get('price')}")

# db.products.update_many({"category" : "Accessories"}, {"$inc" : {"price" : +20}})
# for product in res_eight:
#     print(f"{product.get('name')} - {product.get('price')}")
# #The same 4 rows retrieved BUT with an increment of 20 on their price.

#WIP: Gotta check if the thing above works as intended.

#Exercise 9
#First of all, finding it.
# res_nine_before = db.products.find_one({"name" : "Rain Jacket"})
# print(res_nine_before)

# db.products.update_one({"name" : "Rain Jacket"}, {"$addToSet" : {"tags" : "new"}, "$set" : {"restock_date" : datetime.datetime.now()}})

# res_nine_after = db.products.find_one({"name" : "Rain Jacket"})
# print(res_nine_after)
# #Added the new tag without duplicates - which didn't work before as another "new" was added every time this code ran.
# #Date is represented as ISODate within MongoDB, which corresponds to the time format in the other collections.

#Exercise 10
#First do the check/count.
print(db.orders.count_documents({'order_date' : {"$lt" : datetime.datetime(2026, 3, 20)}}))

db.orders.delete_many({'order_date' : {"$lt" : datetime.datetime(2026, 3, 20)}})

print(db.orders.count_documents({'order_date' : {"$lt" : datetime.datetime(2026, 3, 20)}}))
#Now the count shows 0.
