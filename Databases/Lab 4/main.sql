--Exercise 1
SELECT c.first_name, c.last_name, o.status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id;
--15 rows received.

--Exercise 2
SELECT *
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.first_name = 'Erik'; 
--3 rows received.

--Exercise 3
SELECT *
FROM orders o 
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.city = 'Göteborg'
ORDER BY o.order_date DESC;
--3 rows received.

--Exercise 4
SELECT p.name, p.category
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id;
--23 rows received.

--Exercise 5
SELECT oi.order_id, p.name
FROM order_items oi 
JOIN products p ON oi.product_id = p.product_id
WHERE p.category = 'Shoes';
--4 rows received.

--Exercise 6
SELECT p.name, oi.quantity, oi.unit_price, oi.quantity * oi.unit_price AS line_total
FROM order_items oi 
JOIN products p ON oi.product_id = p.product_id 
WHERE oi.order_id = 10;
--2 rows received.

--Exercise 7
--Alt. 1: Without name specified, going off of product_id.
SELECT c.first_name, o.order_date
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON c.customer_id = o.customer_id
WHERE oi.product_id = 1;

--Alt. 2: Specifically calling the product name.
SELECT c.first_name, o.order_date
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON c.customer_id = o.customer_id
JOIN products p ON p.product_id = oi.product_id
WHERE p.name = 'Hoodie Black';
--3 rows received. 

--Exercise 8
SELECT *
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id;
--17 rows received.

--Exercise 9
SELECT *
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE p.product_id NOT IN 
	(SELECT product_id 
	FROM order_items);
--2 rows received.
	
--Exercise 10
SELECT c.first_name, p.name, oi.quantity 
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
JOIN products p ON p.product_id = oi.product_id
JOIN customers c ON c.customer_id = o.customer_id 
WHERE c.city = 'Uppsala';
--8 rows received.