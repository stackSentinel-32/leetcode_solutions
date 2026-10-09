# Write your MySQL query statement below

with rnkscore as(
    select
    id, 
    score,
    dense_rank() over(order by score desc) as rnk
    from Scores
)

select score,rnk as 'rank'
from rnkscore