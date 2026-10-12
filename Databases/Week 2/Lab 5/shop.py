import sqlite3


def connect():
    conn = sqlite3.connect("webshop.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def list_products(conn):
    cursor = conn.execute("SELECT product_id, name, price, stock FROM products")
    for pid, name, price, stock in cursor.fetchall():
        print(f"{pid:>3}  {name:<20} {price:>8.2f} kr  ({stock} in stock)")


def search_customers(conn):
    city = input("City: ")
    cursor = conn.execute(
        "SELECT first_name, last_name FROM customers WHERE city = ?", (city,))
    rows = cursor.fetchall()
    if not rows:
        print("No customers found.")
    for first, last in rows:
        print(first, last)


def add_product(conn):
    name = input("Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Stock: "))
    conn.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (?, ?, ?, ?)",
        (name, category, price, stock))
    conn.commit()
    print("Saved!")
#Exercise 7 WIP


#Exercise 5
def change_stock(conn):
    product_id = int(input("Product id: "))
    stock = int(input("Stock: "))
    conn.execute(
        "UPDATE products SET stock = ? WHERE product_id = ?",
        (stock, product_id)
    )
    conn.commit()
    print("Stock updated!")

def show_receipt(conn):
    order_id = int(input("Order id: "))
    cursor = conn.execute(
        "SELECT p.name, oi.quantity, oi.unit_price FROM order_items oi JOIN products p ON p.product_id = oi.product_id WHERE oi.order_id = ?", (order_id,)
    )
    #based on the results
    for name, quantity, unit_price in cursor.fetchall():
        print(f'{name}, quantity: {quantity}, unit price: {unit_price}')

def main():
    conn = connect()
    while True:
        print("\n1) List products  2) Search customers  3) Add product 4) Change product stock 5) Show order receipt 0) Quit")
        choice = input("> ")
        if choice == "1":
            list_products(conn)
        elif choice == "2":
            search_customers(conn)
        elif choice == "3":
            add_product(conn)
        #Exercise 5
        elif choice == "4":
            change_stock(conn)
        #Exercise 6
        elif choice == "5":
            show_receipt(conn)
        elif choice == "0":
            break
    conn.close()


main()
