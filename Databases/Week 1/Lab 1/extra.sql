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
SELECT name || ' costs ' || CAST(price as INT) || ' kr' AS price_list
FROM products
WHERE stock > 0
ORDER BY price ASC;

--Exercise 13
SELECT city, COUNT(*) as number_of_customers
FROM customers
GROUP BY city
ORDER BY number_of_customers DESC;