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

--Exercise 7

UPDATE products SET price = price * 1.10 WHERE category = 'Accessories';

--Exercise 8
--SELECT * FROM order_items WHERE order_id IN (SELECT order_id FROM orders WHERE status = 'cancelled');
DELETE FROM order_items WHERE order_id IN (SELECT order_id FROM orders WHERE status = 'cancelled');

--SELECT * FROM orders WHERE status = 'cancelled';

--Each order item has an order_id as a foreign key, so deleting an order will destroy the items' dependencies. Therefore, remove specifically those items first.

--Exercise 9
--SELECT COUNT(*) FROM orders;
--There are 15 entries, so it is correct.

--Exercise 10
--First of all, there is nothing that clearly indicates of any identifier, considering that two students could have the same name.
--Secondly, having the same type of item (within a arguably shared group) multiple times breaks the conditions for 1NF to hold. 
--It would be smarter to have a middle/intermediate table having the primary key as a column consisting of both a student_id and a course.

--Exercise 11
--It breaks 1NF by representing quantity within products, and then having a total not based on a singular price.
--There must be one value per cell in 1NF, so it would make more sense to also have a middle table (inventory),
--where you can tie the order id (foreign key) to a product, and then also have price and quantity. All values are separated, 
--and yet you can still get e.g. the total price by querying a multiplication between the price and quantity.
*/

--Exercise 12

--Exercise 13

--Exercise 14

--Exercise 15

--Exercise 16
--WIP AS THE LAST THING, WE'VE GOT IT.