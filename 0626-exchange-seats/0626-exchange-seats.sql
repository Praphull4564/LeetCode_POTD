select id ,(case when id%2 =1 then lname else rname end) as student from
(select x.id,x.student,x.lid,x.lname,c.id as rid ,(case when c.student is null then x.student else c.student end) as rname from 
(select a.id,a.student,b.id as lid,(case when b.student is null then a.student else b.student end) as lname from Seat a left join Seat b
on b.id=a.id+1 and b.id % 2 = 0)x left join Seat c
on c.id=x.id-1 and c.id % 2 = 1)tb