/*
--LEVEL 1
--Exercise 1
SELECT * 
FROM products
WHERE category IN ('Clothing', 'Accessories')
AND price BETWEEN 150 and 500
ORDER BY price DESC;
--Received 4 rows.

--Exercise 2
SELECT * FROM orders
WHERE strftime('%Y-%m', order_date) = '2026-02'
AND status != 'cancelled';
--Received 4 rows.

--Exercise 3
SELECT oi.order_id, p.name, oi.quantity, oi.quantity * oi.unit_price as line_total
FROM order_items oi 
JOIN products p ON oi.product_id = p.product_id
WHERE line_total > 500
ORDER BY line_total DESC;
--Received 11 rows.

--Exercise 4
SELECT DISTINCT c.first_name
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
WHERE c.city IN ('Stockholm', 'Uppsala');
--Received 5 rows.
*/

--LEVEL 2
--Exercise 5
INSERT INTO customers (first_name, last_name, email, city, joined_date) 
VALUES ("Leo", "Falk", "leofalk@uppsalastad.se", "Uppsala", "2026-10-09");

--Using the email, because it is unique and a piece of imformation that we already have.

INSERT INTO orders (customer_id, order_date)
VALUES (
	(SELECT customer_id 
	FROM customers 
	WHERE email = 'leofalk@uppsalastad.se'), 
	'2026-10-09'
);

INSERT INTO order_items
	(order_id, product_id, quantity, unit_price) 
VALUES 
(
	(SELECT o.order_id FROM orders o JOIN customers c ON o.customer_id = c.customer_id WHERE c.email = 'leofalk@uppsalastad.se' ORDER BY o.order_id),
	(SELECT product_id FROM products WHERE name = 'Hoodie Black'),
	1, 
	(SELECT price FROM products WHERE name = 'Hoodie Black')
);


INSERT INTO order_items
	(order_id, product_id, quantity, unit_price) 
VALUES 
(
	(SELECT o.order_id FROM orders o JOIN customers c ON o.customer_id = c.customer_id WHERE c.email = 'leofalk@uppsalastad.se' ORDER BY o.order_id),
	(SELECT product_id FROM products WHERE name = 'Socks 3-pack'),
	2, 
	(SELECT price * 2 FROM products WHERE name = 'Socks 3-pack')
);

--SELECT * 