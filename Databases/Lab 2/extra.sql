/*
--Level 1
--Exercise 1
CREATE TABLE suppliers (
	supplier_id INTEGER PRIMARY KEY,
	name TEXT UNIQUE NOT NULL,
	country TEXT DEFAULT 'Sweden',
	email TEXT
);

--Exercise 2
INSERT INTO suppliers(supplier_id, name, email)
VALUES (1, 'Nordic Textiles', 'nordictextiles@textilegroup.eu');
--It says 'Sweden', as it is the default value that we specified.

--Exercise 3
INSERT INTO suppliers(supplier_id, name, email)
VALUES (2, 'Nordic Textiles', 'nordictextiles@textilegroup.eu');
--Since the name must be unique, this insertion will not work, because we already have the same name inserted.
*/
--Exercise 4
CREATE TABLE coupons (
	code TEXT PRIMARY KEY,
	discount_percent INTEGER CHECK (discount_percent BETWEEN 1 AND 90),
	valid_until TEXT NOT NULL
);

--Level 2
--Exercise 5

--Exercise 6

--Exercise 7

--Exercise 8

--Exercise 9

--Level 3
--Exercise 10

--Exercise 11

--Exercise 12

--Exercise 13