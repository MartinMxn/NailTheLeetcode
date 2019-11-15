/* Write a query to retrieve the months of 2007 in which  
  there was at least one product sold but no product in white was sold.   
  Sort the returned data by the month. */
 
-- Select the product sell at least one -> JOIN SalesOrderHeader SalesOrderDetail and Product
-- no product in white was sold -> select all month that the product sell in 2007 and color is white, then select the month not in tmp

SELECT DISTINCT month(OrderDate) Month
FROM Sales.SalesOrderHeader
WHERE year(OrderDate) = 2007 AND month(OrderDate) NOT IN
(SELECT DISTINCT MONTH(OrderDate)
 FROM Sales.SalesOrderHeader sh
 JOIN Sales.SalesOrderDetail sd
      ON sh.SalesOrderID = sd.SalesOrderID
 JOIN Production.Product p
      ON p.ProductID = sd.ProductID
 WHERE year(OrderDate) = 2007 AND p.Color = 'White')
ORDER BY Month;

--self
WITH tmp AS (
	SELECT sh.SalesOrderID, MONTH(OrderDate) as [Month]
	FROM Sales.SalesOrderHeader sh
	JOIN Sales.SalesOrderDetail sd
	ON sh.SalesOrderID = sd.SalesOrderID
	JOIN Production.Product p 
	ON p.ProductID = sd.ProductID
	WHERE YEAR(OrderDate) = 2007 AND p.Color = 'White'
)
SELECT DISTINCT MONTH(OrderDate) as [Month]
FROM Sales.SalesOrderHeader s
WHERE MONTH(s.OrderDate) NOT IN (
	SELECT Month FROM tmp
)
ORDER BY Month;
