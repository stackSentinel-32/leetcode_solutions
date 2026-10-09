with rank_em as(
    select
    id,
    salary, 
    Dense_rank() OVER (ORDER BY salary desc) AS rnk
from Employee
)

select max(salary) as SecondHighestSalary
from rank_em
where rnk=2;