select p.product_name,x.unit from Products p join
(select product_id, sum(unit) as unit from Orders
where order_date like "2020-02-__"
group by product_id
)x on x.product_id=p.product_id

where unit>=100
order by unit desc