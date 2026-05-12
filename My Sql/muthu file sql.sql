create database company;
use company;
create table manager(
  man_id int,
  man_name varchar(50),
  gender varchar(50),
  salary int,
  city varchar(50)
  );
  insert into manager 
  values(1,'arun','male',50000,'chennai'),
  (2,'abi','female',60000,'chennai'),
  (3,'barkav','male',65000,'coimbatore'),
  (4,'balaji','male',66000,'bangalore'),
  (5,'chandhra','female',70000,'theni'),
  (6,'chinna','male',77000,'madurai'),
  (7,'darun','male',78000,'ariyalur');
  select * from manager;
  -- this is filter the values
  select count(*)from manager;
   select count(salary)from manager
   where salary >70000;
select * from manager where salary >=70000 and city='ariyalur';
select count(*) from manager where man_name like 'a%';
select count(*) from manager where man_name like '%a';
select count(*) from manager where man_name like '%b%';
select sum(salary) 
from manager
where city='chennai';

   
   