-- PRACTICAL 02 (06-10-22) 

SELECT * FROM CATEGORY;

select * from category;

select * from 'Category';

select * from "Category";

select * from 'category';

select * from "category";

SELECT * FROM “category”;

\d customer


-- create own database task

CREATE DATABASE week02;

CREATE TABLE NEWTABLE(
IAMNUMBER INT PRIMARY KEY,
IAMSTRING VARCHAR(10)
);

INSERT INTO NEWTABLE (IAMNUMBER, IAMSTRING) VALUES(12, 'cheese');

INSERT INTO NEWTABLE (IAMNUMBER, IAMSTRING) VALUES(12, 'ham');