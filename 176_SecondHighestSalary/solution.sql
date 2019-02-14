select max(Salary)
    select max(Salary) as SecondHighestSalary
    where Salary < (select max(Salary) from Employee)


select ifnull((select distinct Salary from Employee order by Salary desc limit 1 offset 1), null) 
    as SecondHighestSalary