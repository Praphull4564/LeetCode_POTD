
select employee_id,department_id from
(select * from Employee left join
(select employee_id as eid,count(distinct department_id) as nd from Employee group by employee_id)x
on x.eid=Employee.employee_id)f
where (primary_flag='Y') or nd=1
order by employee_id