#--print(client.list_database_names())

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

#Exercise 3
res_three = db.products.find()
for product in res_three:
    print(f"{product.get('name')}, {product.get('price')}")
#12 results retrieved.

#Exercise 4
res_four = db.customers.count_documents({'city' : 'Uppsala'})
print(f"Customers in Uppsala: {res_four}")
#Result shows a count of 3, which was expected.

#Exercise 5
res_five = db.products.find_one({'name' : 'Sandals'})
print(f"Stock: {res_five.get('stock')}")
#Result shows 22, which was expected.

#Exercise 6
res_six = db.customers.find({'newsletter' : 'true'})
for customer in res_six:
    print(customer.get('first_name'))

#Exercise 7

#Exercise 8

#Exercise 9

#Exercise 10
