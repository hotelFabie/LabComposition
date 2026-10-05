--1
SELECT first_name, email FROM customers;

--2
SELECT * FROM products WHERE category = 'Shoes';

--3
SELECT * FROM customers WHERE city = 'Uppsala';

--4
SELECT * FROM products WHERE price = 199;

--5
SELECT * FROM products ORDER BY name ASC;

--6
SELECT * FROM customers ORDER BY joined_date DESC;

--7
SELECT * FROM products WHERE stock = 0;

--8
SELECT * FROM customers ORDER BY joined_date DESC LIMIT 3;

--9
SELECT * FROM customers WHERE city IN ('Stockholm', 'Göteborg');

--10
SELECT name, price FROM products;

--BONUS QUESTIONS

--1 "TRY WITHOUT THEM" ???
SELECT * FROM products WHERE category IN ('Clothing', 'Shoes') AND price > 1000;

--2 
SELECT name, price, stock, (price * stock) AS stock_value FROM products WHERE stock > 0;

--3
SELECT * FROM customers WHERE LENGTH(first_name) = 4;

--4
