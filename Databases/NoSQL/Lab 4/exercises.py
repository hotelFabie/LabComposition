from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

#Exercise 1
#While it would be convenient to store all reviews related to one book within the scope of the book.
#However, since a document cannot store a very huge amount of data on its own, 
#referencing review ids in the book would keep data separated not only for what it represents, but also avoiding size limitations. 

#I would probably only reference a member within a review, considering a case where a user may realize that they do not want to publish
#a review under their name, and so they have a chance to rename their account.
#This comes from the perspective of this being a book-related site, like GoodReads, 
#where people have accounts and possibility to remove their content.

#Exercise 2
#Advantage: It gives better cohesion about what the order contains, needing fewer checks across different documents.
#Disadvantage: If the product's name is altered, restructuring the order to adhere to the current name will be more tedious.

#Exercise 3
# db.create_collection("newsletter_signups", validator={"$jsonSchema": { 
#     "required" : ["email"],
#     "properties" : {
#         "_id" : {"bsonType" : "objectId"},
#         "email" : {"bsonType" : "string"},
#         "source" : {
#             "enum": ["web", "store"]
#         }
#     }
# }})

#Valid insertion
# db.newsletter_signups.insert_one({"email" : "valid@val.id", "source" : "store"})

#Invalid insertion
# db.newsletter_signups.insert_one({"source" : "forest"})

#Exercise 4
# res_four = db.customers.aggregate([
#     {
#         "$group" : {
#             "_id": "$city", 
#             "customers" : {"$sum" : 1}
#         }
#     },
#     {
#         "$sort" : {"city" : -1}
#     }
# ])

# for city in res_four:
#     print(city)
# #6 rows retrieved, with giving None as a city.

# #Exercise 5
# res_five = db.products.aggregate([
#     {
#         "$group": {
#             "_id" : "$category",
#             "maximum" : {"$max": "$price"},
#             "minimum" : {"$min": "$price"}
#         }
#     }
# ])
# #3 rows retrieved.

# for product in res_five:
#      print(product)

# #Exercise 6
# res_six = db.orders.aggregate([
#     {"$match" : {"orders" : {"$gte" : 2}}},
#     {"$group" : {
#         "_id" : "$customer_id",
#         "orders" : {"$sum" : 1}}},
# ])

# for order in res_six:
#     print(order)
# #5 rows retrieved.

# #Exercise 7
# res_seven = db.orders.aggregate([
#     {
#         '$project': {
#             "_id" : "$_id",
#             "item_count" : {"$size" : "$items"}
#         }
#     }
# ])

# for order in res_seven:
#     print(order)
# #15 rows retrieved.

#Switched to writing the pipeline separately.
#Exercise 8
res_eight = [
    {"$unwind" : "$items"},
    
    {
        "$lookup" : {
            "from" : "products",
            "localField": "items.product_id",
            "foreignField": "_id",
            "as": "product"
        }
    },
    
    {"$unwind" : "$product"},
    
    {
        "$group" : {
            "_id": "$product.category",
            "units" : {"$sum" : "$items.quantity"}
        }
    }
]

for order in db.orders.aggregate(res_eight):
    print(order)