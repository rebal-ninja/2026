use cse_d;


alter table student add age int;
desc student;

alter table student modify column CGPA int;
alter table student modify column name varchar(10);


use cse_d;
show tables ;
desc student_info;

alter table student rename column name to student_name ;

alter table student drop column age ;

rename table student to student_info ;

insert into student_info (roll_no,student_name,CGPA) values (351,"tez",9.6);
show tables;

select *from student_info;
insert into student_info (roll_no,student_name,CGPA) values 
(355,"pavan",8),(359,"raj",8),(219,"divya",8),(204,"yashavi",9);  

