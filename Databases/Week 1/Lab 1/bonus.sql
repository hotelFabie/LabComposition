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