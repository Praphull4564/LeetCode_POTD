select dname as Department, name as Employee, salary as Salary
from (select * from 
(select dname,name,salary,dense_rank() over (partition by dId order by salary desc) as rnk 
from
(select * from Employee e join (select id as dId,name as dname from Department) d on e.departmentId=d.dId)t
)x
where rnk=3 or rnk=2 or rnk=1)y