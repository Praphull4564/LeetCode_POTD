
select name as Customers from 
(select * from Customers c left join (select customerId from Orders) o on c.id = o.customerId) as t 
where 
t.customerId is null