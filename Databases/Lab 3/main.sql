/*
--Exercise 1
INSERT INTO customers VALUES (11, 'Fabian', 'V.', 'fbao@yo.kp', 'Stockholm', '2026-10-07');

--Exercise 2
INSERT INTO products VALUES (13, 'Scarf', 'Accessories', 229, 15), 
	(14, 'Gloves', 'Accessories', 199, 20);
	
--Exercise 3
INSERT INTO orders (order_id, customer_id, order_date) VALUES (16, 7, '2026-10-07');

INSERT INTO order_items VALUES (16, 10, 2, 179); 

--Exercise 4
INSERT INTO orders VALUES (17, 1, '2026-10-07', 0);
--The rule that stops this from happening is the check on the quantity requiring it to be above 0, and we are currently inserting 0, which will be denied.

--Exercise 5
UPDATE orders SET status = 'shipped' WHERE order_id = 12;

--Exercise 6
--SELECT * FROM products WHERE product_id = 5;
UPDATE products SET stock = 50 WHERE product_id = 5;
*/

--Exercise 7

--Exercise 8

--Exercise 9

--Exercise 10

--Exercise 11

--Exercise 12

--Exercise 13

--Exercise 14

--Exercise 15

--Exercise 16