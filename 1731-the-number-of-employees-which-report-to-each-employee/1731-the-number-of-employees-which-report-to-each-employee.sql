
select employee_id,name,count(reportFrom) as reports_count,round(avg(age),0) as average_age from
(select * from (select employee_id,name from Employees )e1 
join (select employee_id as reportFrom,age,reports_to from Employees )e2
on e1.employee_id=e2.reports_to)f
group by employee_id
order by employee_id