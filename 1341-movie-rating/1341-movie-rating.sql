
(select min(name) as results from
(select user_id,count(distinct movie_id) as cnt from MovieRating
group by user_id)x join Users u
on x.user_id=u.user_id
group by cnt
order by cnt desc
limit 1)

union all

(select min(title) as results from
(select movie_id,avg(rating) as ar from MovieRating 
where created_at like '2020-02-__'
group by movie_id)x join Movies m
on x.movie_id = m.movie_id
group by ar
order by ar desc limit 1)