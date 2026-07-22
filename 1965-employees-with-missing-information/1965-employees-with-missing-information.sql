select employee_id from (
SELECT (case when e.employee_id is not null then e.employee_id else s.employee_id end) as employee_id,name,salary
FROM Employees e
LEFT JOIN Salaries s
    ON e.employee_id = s.employee_id

UNION

SELECT (case when e.employee_id is not null then e.employee_id else s.employee_id end) as employee_id,name,salary
FROM Employees e
RIGHT JOIN Salaries s
    ON e.employee_id = s.employee_id)t

where t.name is null or t.salary is null
order by employee_id