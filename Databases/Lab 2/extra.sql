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

--Exercise 4
CREATE TABLE coupons (
	code TEXT PRIMARY KEY,
	discount_percent INTEGER CHECK (discount_percent BETWEEN 1 AND 90),
	valid_until TEXT NOT NULL
);

INSERT INTO coupons (code, discount_percent, valid_until) 
VALUES ('AUTUMN95', 95, '2026-10-31');
--This will not work, because of the constraint that the discount percent must be between 1 and 90, and 95 is above that.

--Level 2
--Exercise 5
INSERT INTO suppliers (name, email) 
VALUES ('Moom', 'moom@jambakery.nz');
--It will give it the next available value in ascending numerical order. 
--As we only have had an entry where the primary key value is 1, we get 2 as the id for this insertion.

--Exercise 6
ALTER TABLE suppliers RENAME COLUMN email TO contact_email;

--Exercise 7
PRAGMA table_info(suppliers);
*/

--Exercise 8

--Exercise 9

--Level 3
--Exercise 10

--Exercise 11

--Exercise 12

--Exercise 13