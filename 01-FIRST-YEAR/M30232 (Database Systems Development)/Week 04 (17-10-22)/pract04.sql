-- FIRST TASK: COPY CODE BELOW INTO THE PSQL PROMPT AND RUN IT
CREATE DATABASE customer_db;

\c customer_db

CREATE TABLE customer1 (cust_id SERIAL PRIMARY KEY, cust_fname VARCHAR(20) NOT NULL, cust_lname VARCHAR(20) NOT NULL);

\d customer1

ALTER TABLE customer1 ADD COLUMN cust_email varchar(100) NOT NULL UNIQUE;

\d customer1



DROP TABLE customer1;

-- check that the table is gone now

-- anything in the line after the two dashes is a comment by the way

\l
\d customer1



CREATE TABLE customer (cust_id SERIAL PRIMARY KEY, cust_fname VARCHAR(20) NOT NULL, cust_lname VARCHAR(20) NOT NULL, cust_email varchar(60) NOT NULL);


INSERT INTO customer (cust_id, cust_fname, cust_lname, cust_email) VALUES (22,'Kamil', 'Novák','kamnovák@gmail.com');

INSERT INTO customer (cust_id, cust_fname, cust_lname, cust_email) VALUES (66,'Aarav', 'Anand','aanand98@gmail.com');

INSERT INTO customer (cust_id, cust_fname, cust_lname, cust_email) VALUES (67,'Alia', 'Anand','aanand98@gmail.com');


SELECT * FROM customer;

SELECT cust_fname, cust_email from customer;


SELECT cust_email, cust_id, cust_fname, cust_lname from customer;


UPDATE customer SET cust_email = 'i_love_elephants_1@gmail.com' where cust_id = 66;
SELECT * FROM customer;

INSERT INTO customer (cust_id, cust_fname, cust_lname, cust_email) VALUES (67,'Alia', 'Anand','aanand98@gmail.com');


INSERT INTO customer (cust_id, cust_fname, cust_lname, cust_email) VALUES (70,'Connor', 'Murphy','connormurphy99@gmail.com');

INSERT INTO customer (cust_id, cust_fname, cust_lname, cust_email) VALUES (71,'Connor', 'Murphy','connormurphy199@gmail.com');

INSERT INTO customer (cust_id, cust_fname, cust_lname, cust_email) VALUES (1,'Tim', 'Nice-but-Dimm','alongemailaddresswillfit@quitealongdomainnametoo.com');

INSERT INTO customer ( cust_fname, cust_lname, cust_email) VALUES ('Tim', 'Nice-but-Dimm','averylongemailaddresswillnotfit11111111111111111111111111111111111111111a@quitealongdomainnametoo.com');




-- TASK 2: Write code for various things

CREATE DATABASE code_test;
\c code_test

CREATE TABLE table_one(Record_id INT PRIMARY KEY, Att_1 VARCHAR(30), Att_2 CHAR(10), Att_3 DECIMAL(3,2));
\d table_one
/*
                      Table "public.table_one"
  Column   |         Type          | Collation | Nullable | Default
-----------+-----------------------+-----------+----------+---------
 record_id | integer               |           | not null |
 att_1     | character varying(30) |           |          |
 att_2     | character(10)         |           |          |
 att_3     | numeric(3,2)          |           |          |
Indexes:
    "table_one_pkey" PRIMARY KEY, btree (record_id)

*/

ALTER TABLE table_one ADD COLUMN Att_4 INT;
\d table_one
/*
                      Table "public.table_one"
  Column   |         Type          | Collation | Nullable | Default
-----------+-----------------------+-----------+----------+---------
 record_id | integer               |           | not null |
 att_1     | character varying(30) |           |          |
 att_2     | character(10)         |           |          |
 att_3     | numeric(3,2)          |           |          |
 att_4     | integer               |           |          |
Indexes:
    "table_one_pkey" PRIMARY KEY, btree (record_id)
*/

INSERT INTO table_one (Record_id, Att_1, Att_2, Att_3, Att_4) VALUES (1, 'continent', '0olP$fguj', 9.99, 42);
INSERT INTO table_one (Record_id, Att_1, Att_2, Att_3, Att_4) VALUES (2, 'Portsmouth University', 'Violet', 9.99, 9999);
SELECT * FROM table_one;
/*
 record_id |         att_1         |   att_2    | att_3 | att_4
-----------+-----------------------+------------+-------+-------
         1 | continent             | 0olP$fguj  |  9.99 |    42
         2 | Portsmouth University | Violet     |  9.99 |  9999
(2 rows)
*/

UPDATE table_one SET Att_4 = 66 WHERE record_id = 1;
SELECT * FROM table_one WHERE record_id = 1;

/*
 record_id |   att_1   |   att_2    | att_3 | att_4
-----------+-----------+------------+-------+-------
         1 | continent | 0olP$fguj  |  9.99 |    66
(1 row)
*/
