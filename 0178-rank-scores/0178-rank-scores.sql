# Write your MySQL query statement below
select round(score,2) as score, 
dense_rank() over (order by score desc) as 'rank'
from Scores 