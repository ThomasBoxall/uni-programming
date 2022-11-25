SELECT cust_fname, cust_lname from customer;

SELECT cust_fname, cust_lname, town FROM customer;

SELECT cust_fname, cust_lname FROM customer WHERE town= 'La Mohammedia';

SELECT * FROM category;

SELECT cat_id from category where cat_name='Sport';

SELECT product.prod_name, category.cat_name FROM product
JOIN category ON category.cat_id = product.prod_cat;

SELECT staff.staff_fname, staff.staff_lname, staff.work_email, role.role_name from staff
JOIN role ON staff.role = role.role_id;

SELECT staff.staff_lname, role.role_name, cust_order.cust_ord_id, customer.cust_fname, customer.cust_lname FROM staff
JOIN role ON staff.role = role.role_id
JOIN cust_order ON cust_order.staff_id = staff.staff_id
JOIN customer ON customer.cust_id = cust_order.cust_id
WHERE customer.cust_lname = 'Eke';

SELECT customer.cust_lname, category.cat_name FROM customer
JOIN cust_order ON customer.cust_id = cust_order.cust_id
JOIN manifest ON cust_order.cust_ord_id = manifest.cust_ord_id
JOIN product ON product.prod_id = manifest.prod_id
JOIN category ON category.cat_id = product.prod_cat
WHERE customer.town = 'Sunbu';

SELECT customer.cust_lname, count(category.cat_name), category.cat_name FROM customer
JOIN cust_order ON customer.cust_id = cust_order.cust_id
JOIN manifest ON cust_order.cust_ord_id = manifest.cust_ord_id
JOIN product ON product.prod_id = manifest.prod_id
JOIN category ON category.cat_id = product.prod_cat
GROUP BY customer.cust_lname, category.cat_name, customer.town
HAVING customer.town='Sunbu';