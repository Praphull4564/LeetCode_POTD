select employee_id from
(select e.employee_id,e.manager_id,e.salary,f.employee_id as maid from
Employees e left join Employees f
on e.manager_id=f.employee_id )x
where salary<30000 and maid is null and manager_id is not null
order by employee_id