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

--BONUS QUESTIONS

--How products that are Clothing or Shoes **and** cost more than 1000 kr. Hint: you need brackets. Try without them too: why is the answer different?
--1 

SELECT * FROM products 
WHERE (category = 'Clothing' OR category = 'Shoes') AND price > 1000;
--Without the parenthesis/brackets, it will check for either 1) things in the category clothing, 2) things in the category shoes with price > 1000.
--The price condition will not be applied for both categories, and so we will get 7 rows instead of 3 without the brackets.

--For every product in stock, show name, price, stock and the total value of the stock (price × stock) as `stock_value`. Highest value first. 
--2 
SELECT name, price, stock, (price * stock) AS stock_value FROM products 
WHERE stock > 0;

--Which customers have a first name with exactly 4 letters? Hint: `_` in LIKE means "exactly one character".
--3
SELECT * FROM customers 
WHERE first_name LIKE '____';

--Sort the products by price, cheapest first, and show only products number 6 to 10. Hint: look up `OFFSET`.
--4
SELECT * FROM products
ORDER BY price ASC LIMIT 5 OFFSET 5;

--Show customers who joined before 2025 and don't live in Uppsala. Sort by city, and by last name within the same city.
--5 
SELECT * FROM customers 
WHERE city != 'Uppsala' AND joined_date < 2025 
ORDER BY city ASC, last_name DESC;

--EXTRA CHALLENGES

--LEVEL 1
--Exercise 1
SELECT * FROM products
WHERE category != 'Accessories' AND stock > 0 AND name LIKE '% %'
ORDER BY category, price DESC;

--Exercise 2
SELECT * FROM customers
WHERE city LIKE 'S%' OR city LIKE 'M%' OR city IS NULL;

--Exercise 3
SELECT * FROM products 
WHERE category = 'Shoes'
ORDER BY price DESC
LIMIT 1 OFFSET 1;

--Exercise 4
SELECT * FROM customers
WHERE joined_date LIKE '2024%' OR joined_date LIKE '2025%'
ORDER BY joined_date DESC
LIMIT 3;


--LEVEL 2
--Exercise 5
SELECT first_name || ', ' || last_name AS full_name FROM customers  
ORDER BY last_name;

--Exercise 6
SELECT *, price,
CASE
	WHEN price < 200 THEN 'budget'
	WHEN price >= 200 AND price <= 799 THEN 'mid' 
	WHEN price > 800 THEN 'premium'
END AS price_level
FROM products; 

--Exercise 7
SELECT first_name, COALESCE(city, 'Unknown') AS city
FROM customers;

--Exercise 8
SELECT *
FROM customers
WHERE strftime('%m', joined_date) BETWEEN '01' AND '06';

--Exercise 9
SELECT * FROM products
ORDER BY LENGTH(name) DESC
LIMIT 1;

--Exercise 10
SELECT substr(email, 0, instr(email, '@')) AS 'email_username'
FROM customers;

--LEVEL 3
--Exercise 11
SELECT *
FROM products
WHERE price > (SELECT avg(price) FROM products);

--Exercise 12


--Exercise 13