/* Write your T-SQL query statement below */
WITH tmp AS (
    SELECT 
        d.Name as Department,
        e.Name as Employee,
        e.Salary as Salary,
        DENSE_RANK() OVER(Partition by d.Name Order by e.Salary Desc) as R
    FROM Employee e
    JOIN Department d
    ON e.DepartmentId = d.Id
    GROUP by d.Name, e.Name, e.Salary
)
SELECT Department, Employee, Salary
FROM tmp
WHERE R < 4
