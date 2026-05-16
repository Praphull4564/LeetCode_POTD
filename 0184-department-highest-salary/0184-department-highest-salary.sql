select m.dname as Department,e.name as Employee,e.salary as Salary from 
(select did,dname,max(salary) as msal from ((select id as did,name as dname from Department) d left join Employee e on e.departmentId=d.did) group by dname) m, Employee e
where e.salary=m.msal and m.did=e.departmentId