
select requester_id as id , count(distinct accepter_id) as num from
(select * from RequestAccepted 
union all
select accepter_id as requester_id ,requester_id as accepter_id ,  accept_date
from RequestAccepted)x
group by id
order by num desc
limit 1