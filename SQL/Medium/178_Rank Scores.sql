/* Write your T-SQL query statement below */
SELECT 
    Score, 
    DENSE_RANK() over (ORDER BY Score DESC) as Rank
FROM Scores
