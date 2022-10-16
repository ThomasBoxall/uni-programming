SELECT COUNT(*) FROM ROLE;

INSERT INTO ROLE (ROLE_NAME) VALUES ('Pre Sales');

 SELECT * FROM ROLE;

select count(*) from category;
select count(*) from cust_order;
select count(*) from customer;
select count(*) from manifest;
select count(*) from product;
select count(*) from role;
select count(*) from staff;

select max(role_id) from role;

select count(*) from role;

DELETE FROM ROLE WHERE ROLE_NAME = 'Pre Sales'; 

INSERT INTO ROLE (ROLE_NAME) VALUES ('Cleaning Team');

SELECT RANDOM(); 

select random()*11;

create table numb1(numb_id int primary key, ran_val decimal(17,15));

insert into numb1(numb_id, ran_val) values
(1,random()),(2,random()),(3,random()),(4,random()),(5,random()),(6,random()),(7,random()),(8,random()),(9,random()),(10,random());

SELECT COUNT(*) FROM NUMB1;

SELECT * FROM NUMB1;

select max(ran_val) from numb1;

select min(ran_val) from numb1;

select avg(ran_val) from numb1;

select now();

select cust_fname from customer where cust_id=3;

select cat_id from category where cat_name='Outdoor';

select count(*) from cust_order where cust_id=15;

select staff_fname, staff_lname from staff where town='Portsmouth';

select addr1 , addr2 from staff where staff_id=4;

select count(*) from staff where role=3;

select count(*) from product where prod_id=2;