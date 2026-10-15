#This file will be used to quickly reset the database, 
# so that we always have a base case in terms of what data we are dealing with.

from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["library"] 

#Base books
books = [
    {"_id": 1, "title": "Convenience Store Woman", "author": "Sayaka Murata", "genres": ["fiction", "slice-of-life"], "stock" : 3, "reviews": []},
    {"_id": 2, "title": "x", "author": "y", "genres": ["z", "a"], "stock" : 1, "reviews": []},
    {"_id": 3, "title": "x", "author": "y", "genres": ["z", "a"], "stock" : 1, "reviews": []},
    {"_id": 4, "title": "x", "author": "y", "genres": ["z", "a"], "stock" : 2, "reviews": []},
    {"_id": 5, "title": "x", "author": "y", "genres": ["z", "a"], "stock" : 1, "reviews": []}
]

#Base members
members = [
    {"_id": 1, "first_name": "May", "last_name": "Jane", "email": "mayjane@bliss.eu", "loaned_books": []},
    {"_id": 2, "first_name": "Mason", "last_name": "Square", "email": "masonsquare@jotunheim.no", "loaned_books": []},
    {"_id": 3, "first_name": "Chou", "last_name": "Chou", "email": "cc@butterflycorp.org", "loaned_books": []}
]
for name in ["books", "members"]:
    db[name].drop()

db.books.insert_many(books)
db.members.insert_many(members)