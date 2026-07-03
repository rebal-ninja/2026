CREATE DATABASE idk;

SHOW databases;

USE idk;

create table students (
id int primary key ,
name varchar(50),
age int ,
department varchar(30)
);

show tables;

describe students;


insert into students (id, name, age) values (1,"aman",17,"cse");
insert into students (id, name, age) values (2,"tez",18,"ece");
INSERT INTO students (id, name, age) VALUES (3, 'Karan', 18);


SELECT * FROM students;



INSERT INTO students VALUES (4, 'Test', 20, 'MECH');
COMMIT;
SELECT * FROM students;
