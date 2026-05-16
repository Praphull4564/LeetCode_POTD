
select EMP.name as Employee
from Employee EMP, Employee MGR
where 
(MGR.salary<EMP.salary)and(MGR.id=EMP.managerId)
