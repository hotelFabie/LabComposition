--Show the first name and email of all customers.
--1
SELECT first_name, email FROM customers;

--Show all products in the Shoes category.
--2
SELECT * FROM products 
WHERE category = 'Shoes';

--Which customers live in Uppsala? 
--3
SELECT * FROM customers 
WHERE city = 'Uppsala';

--Which product costs exactly 199 kr?
--4
SELECT * FROM products 
WHERE price = 199;

--Show all products sorted by name, A to Z.
--5
SELECT * FROM products 
ORDER BY name ASC;

--Show all customers, the one who joined first at the top.
--6
SELECT * FROM customers 
ORDER BY joined_date DESC;

--Which products are sold out (stock is 0)?
--7
SELECT * FROM products 
WHERE stock = 0;

--Show the 3 newest customers.
--8
SELECT * FROM customers 
ORDER BY joined_date DESC LIMIT 3;

--Show customers from Stockholm or Göteborg. Use IN.
--9
SELECT * FROM customers 
WHERE city IN ('Stockholm', 'Göteborg');

--Show product name and price, but call the columns `product` and `price_sek`.
--10
SELECT name AS 'product', price AS 'price_sek' FROM products;