select f.customer_id from
(select * from Customer join
(select count(*) as cnt from Product)x)f
group by customer_id
having count(distinct product_key)=max(cnt)