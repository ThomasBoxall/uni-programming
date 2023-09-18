-- Queries written as part of completing worksheet

SELECT * FROM customer;

SELECT * FROM staff;

-- Random queries written during session as reading PSQL docs

SELECT staff_fname, staff_lname FROM staff;

SELECT * FROM category WHERE cat_id>3;

SELECT * FROM category
ORDER BY cat_name;

SELECT * FROM product;

SELECT * FROM category JOIN product ON cat_id=prod_cat;