--DDL TABLES 

CREATE TABLE public.hired_employees (
	id int4 NULL,
	nombre varchar(255) NULL,
	fecha_contrato timestamptz NULL,
	department_id int4 NULL,
	job_id int4 NULL
);


create table public.departments (
	id int4 NULL,
	department varchar(255) NULL
);

create table public.jobs (
	id int4 NULL,
	job varchar(255) NULL
);

----SQL QUESTION 1
select 
b.department,
c.job,  
SUM(case when extract(quarter from a.fecha_contrato) =1  then 1 ELSE 0 end) as Q1,
SUM(case when extract(quarter from a.fecha_contrato) =2  then 1 ELSE 0 end) as Q2,
SUM(case when extract(quarter from a.fecha_contrato) =3  then 1 ELSE 0 end) as Q3,
SUM(case when extract(quarter from a.fecha_contrato) =4  then 1 ELSE 0 end) as Q4
from public.hired_employees a 
inner join public.departments b on a.department_id =b.id 
inner join public.jobs c on a.job_id =c.id
where a.fecha_contrato >='2021-01-01' and  a.fecha_contrato <'2022-01-01'
group by 1,2
order by b.department,c.job;  



----SQL QUESTION 2

with dep_hire as (
select b.department,count(1) q_hires 
from public.hired_employees a 
inner join public.departments b on a.department_id =b.id 
inner join public.jobs c on a.job_id =c.id
where a.fecha_contrato >='2021-01-01' and  a.fecha_contrato <'2022-01-01'
group by 1
)
select b.department,count(1) q_hires  
from public.hired_employees a 
inner join public.departments b on a.department_id =b.id 
inner join public.jobs c on a.job_id =c.id
--where a.fecha_contrato >='2021-01-01' and  a.fecha_contrato <'2022-01-01'
group by 1
having count(1) > (select avg(q_hires) from dep_hire)
order by 2 desc;
