/* Write your T-SQL query statement below */
WITH tmp AS(
    SELECT 
        d.Name as [Department], 
        e.Name as [Employee], 
        e.Salary, 
        DENSE_RANK() over (PARTITION BY d.Name ORDER BY e.Salary DESC) AS Rank
    FROM Employee e 
    JOIN Department d
    ON e.DepartmentId = d.Id
)
SELECT Department, Employee, Salary
FROM tmp
WHERE Rank = 1
ORDER BY Salary DESC
