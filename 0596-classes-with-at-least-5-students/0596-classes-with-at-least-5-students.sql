select class from
(select class,count(student) as cnt from Courses group by class)t
where t.cnt>=5