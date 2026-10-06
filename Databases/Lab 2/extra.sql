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

--Exercise 8
CREATE TABLE product_suppliers (
	product_id INTEGER NOT NULL,
	supplier_id INTEGER NOT NULL, 
	purchase_price REAL NOT NULL CHECK (purchase_price > 0),
	PRIMARY KEY (product_id, supplier_id),	
	FOREIGN KEY (product_id) REFERENCES products(product_id),
	FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
);

INSERT INTO product_suppliers (product_id, supplier_id, purchase_price) 
VALUES (1, 99, 0.01);
--It fails, because there is no supplier with id 99, so there can't be no tie to nothing.

--Exercise 9
CREATE TABLE campaigns (
	name TEXT PRIMARY KEY, 
	start_date TEXT,
	end_date TEXT CHECK (end_date > start_date)
);

--Test
INSERT INTO campaigns (name, start_date, end_date) 
VALUES ('kool-aid big pack', '2026-10-06', '2026-10-05');
--Won't work, because of the constraint. In order words, it DOES work as we want it to! :D 

--Level 3
--Exercise 10
CREATE TABLE product_sizes (
	id INTEGER PRIMARY KEY,
	product_id INTEGER UNIQUE NOT NULL,
	size TEXT UNIQUE NOT NULL CHECK (size IN ('S', 'M', 'L', 'XL')),
	stock INTEGER DEFAULT 0,
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);

--Test
INSERT INTO product_sizes (id, product_id, size, stock) 
VALUES (1, 1, 'S', 7);

INSERT INTO product_sizes (id, product_id, size, stock) 
VALUES (2, 1, 'S', 5);
--This will not work - which is expected - since the product already has one size.
*/


--Exercise 11

--Exercise 12
