select r.contest_id , round((count(r.user_id)/cnt)*100,2) as percentage
from (select count(*) as cnt from Users) u , Register r
group by r.contest_id
order by percentage desc,contest_id asc