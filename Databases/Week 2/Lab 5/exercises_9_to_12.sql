--Exercise 9 

/*
--Since it is mentioned that Anna is customer 1, I go off of the id and skip a lookup based on her name.
SELECT p.name FROM order_items oi 
JOIN orders o ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE o.customer_id = 1;
--Received 4 rows.

--Exercise 10
UPDATE customers 
SET email = 'erik.johansson@example.com'
WHERE customer_id = 2;
--Updated as expected.

--Exercise 11
CREATE VIEW customer_overview AS 
SELECT c.customer_id, c.first_name, c.city, COUNT(o.order_id) AS number_of_orders
FROM customers c 
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id;

SELECT * FROM customer_overview;
*/

--Exercise 12
--Within Europe, if you are to follow GDPR, there should never be any reason to collect more data than what is needed, nor have it persist longer than needed.
--Considering a case where date of birth is inserted, storing it without a clear motive also allows it to be used for malicious or external intents.