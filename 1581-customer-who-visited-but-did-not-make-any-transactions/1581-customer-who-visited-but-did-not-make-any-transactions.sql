
select customer_id, count(*) as count_no_trans from 
(select v.visit_id,v.customer_id,t.transaction_id from Visits v left join Transactions t on v.visit_id=t.visit_id)t
where transaction_id is null 
group by customer_id

