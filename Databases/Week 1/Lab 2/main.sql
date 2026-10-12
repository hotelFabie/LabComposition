--Exercise 1 
CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT, 
	year INTEGER
);

--Exercise 2 
DROP TABLE books;

CREATE TABLE books (
	book_id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	author TEXT, 
	year INTEGER CHECK (year > 1400)
);

--Exercise 3 
ALTER TABLE books ADD COLUMN isbn TEXT;

--Exercise 4 
DROP TABLE books;

--Exercise 5 
CREATE TABLE reviews (
	review_id INTEGER PRIMARY KEY,
	product_id INTEGER NOT NULL,
	rating CHECK (rating BETWEEN 1 AND 5),
	comment TEXT,
	FOREIGN KEY (product_id) REFERENCES products(product_id)
);

--Exercise 6 
INSERT INTO reviews (review_id, product_id, rating, comment) 
VALUES(1, 1, 6, "AMAZING!");
--It will not work, because the check for the rating limits it to be between the interval of 1-5.

--Exercise 7 
INSERT INTO reviews (review_id, product_id, rating, comment) 
VALUES(2, 50, 4, 'satisfying.');
--It will not work, because it will look on the foreign key - product_id - and realize that there is no product with id 50 (up to 12 as of right now).

--Exercise 8 
--Look at the image of the drawn paper in this folder.
