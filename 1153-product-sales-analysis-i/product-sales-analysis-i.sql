# Write your MySQL query statement below
select c.product_name, s.year,s.price
from Sales s
join Product c
on s.product_Id=c.product_Id