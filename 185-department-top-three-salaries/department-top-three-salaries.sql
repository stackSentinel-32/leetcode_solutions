select d.name as Department,e.name as Employee,e.salary AS Salary  
from(  
    select name , salary, departmentId,  
    Dense_rank() over (  
        partition by departmentId  
        order by salary desc  
    ) as rnk  
    from Employee  
) e  
join Department d  
on e.departmentId=d.id  
where e.rnk<=3  
