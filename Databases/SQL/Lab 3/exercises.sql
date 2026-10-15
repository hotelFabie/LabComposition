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

--Exercise 12
--The incorrect column is customer_email, because you should be able to extract it with the customer_id, which should be a foreign key to a customer table, containing
--all relevant information about the customer. 

--Exercise 13
--__Students__ take __lessons__ from __teachers__. 
--__Lesson__ has a date, time, room and __instrument__. 
--One __teacher__ can teach many __instruments__.

--Exercise 14
--Student-Lesson: N:M (Students can have many lessons, and lessons can have many students.)
--Teacher-Lesson: 1:N (A teacher can have many lessons, and a lesson is held by one teacher.)
--Teacher-Instrument: N:M (A teacher can play many instruments, and and instrument can be played by different teachers.)
--Instrument-Lesson: 1:N (An instrument can be part of many lessons, and a lesson focuses on one instrument.)

--***
--Written answers on paper also exist in exercise10_to_14.jpg.
--***
--Exercise 15
--Written on paper, provided in the same directory as this file.

--Exercise 16
--Result provided in music.db, in the same directory.

CREATE TABLE students (
	student_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE teachers (
	teacher_id INTEGER PRIMARY KEY,
	name TEXT NOT NULL
);


CREATE TABLE instruments (
	instrument_id INTEGER PRIMARY KEY,
	name TEXT UNIQUE NOT NULL
);

CREATE TABLE lessons ( 
	lesson_id INTEGER PRIMARY KEY,
	teacher_id INTEGER NOT NULL,
	lesson_date TEXT NOT NULL,
	lesson_time TEXT NOT NULL,
	lesson_room TEXT NOT NULL,
	FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) 
);
--Had this table above get attribute names that were a bit long but cohesive, because date and time was marked as keywords.

CREATE TABLE students_lessons(
	student_id INTEGER NOT NULL,
	lesson_id INTEGER NOT NULL, 
	PRIMARY KEY (student_id, lesson_id),
	FOREIGN KEY (student_id) REFERENCES students(student_id),
	FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id)
);

CREATE TABLE teachers_instruments(
	teacher_id INTEGER NOT NULL,
	instrument_id INTEGER NOT NULL, 
	PRIMARY KEY (teacher_id, instrument_id),
	FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id),
	FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
);

--In case something goes wrong.
/*
DROP TABLE students;
DROP TABLE teachers;
DROP TABLE lessons;
DROP TABLE instruments;
DROP TABLE students_lessons;
DROP TABLE teachers_instruments;
*/