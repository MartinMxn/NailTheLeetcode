CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    SET N = N - 1;
  RETURN (
      # Write your MySQL query statement below.
      SELECT
      DISTINCT Salary FROM Employee
      ORDER BY Salary DESC
      LIMIT N, 1  #offset, count. And count start from 0, so make N to N - 1
  );
END
