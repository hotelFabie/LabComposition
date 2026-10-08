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
--So far 21 rows, so something is not correct.

--Exercise 5
SELECT oi.order_id, p.name
FROM order_items oi 
JOIN products p ON oi.product_id = p.product_id
WHERE p.category = 'Shoes';
--4 rows received.

--Exercise 6

--Exercise 7

--Exercise 8

--Exercise 9

--Exercise 10

