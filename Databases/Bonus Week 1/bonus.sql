--LEVEL 1
--Exercise 1
SELECT * 
FROM products
WHERE category IN ('Clothing', 'Accessories')
AND price BETWEEN 150 and 500
ORDER BY price DESC;

--Exercise 2
SELECT * FROM orders
WHERE strftime('%Y-%m', order_date) = '2026-02'
AND status != 'cancelled';

--Exercise 3
SELECT oi.order_id, p.name, oi.quantity, oi.quantity * oi.unit_price as line_total
FROM order_items oi 
JOIN products p ON oi.product_id = p.product_id
WHERE line_total > 500
ORDER BY line_total DESC;

--Exercise 4


