import sqlite3

conn = sqlite3.connect("webshop.db")
cursor = conn.cursor()

# #Exercise 1
# cursor.execute("SELECT first_name, last_name, city FROM customers")
# for first, last, city in cursor.fetchall():
#     print(f'{first} {last} ({city})')

# #Exercise 2
# max_price = float(input("give a max price>"))
# cursor.execute("SELECT name, price FROM products WHERE price < ?", (max_price,))
# for name, price in cursor.fetchall():
#     print(f'{name} - {price}')

# #Exercise 3
# category = input("give a category>")
# cursor.execute("SELECT COUNT(*) FROM products WHERE category = ?", (category,))
# for count in cursor.fetchone():
#     print(f'number of products in the {category} category: {count}')

#Exercise 4
#Using an f-string for SQL code means that whatever you pass in within the SQL query will be treated as SQL code.
#That means that a variable could have a query that allows unintended actions within the database, because you add behavior.
#Using a placeholder "?" will instead make sure that whatever is passed is treated as data values, and not as something part of how the query is structured.

#Exercises 5-8 are done in shop.py
#Exercises 9-12 are done in exercises_9_to_12.sql

conn.close()