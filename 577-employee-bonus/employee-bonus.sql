select e.name,b.bonus 
from Employee e
Left join Bonus b
ON e.empId=b.empId
Where b.bonus<1000 or b.bonus is NULL;