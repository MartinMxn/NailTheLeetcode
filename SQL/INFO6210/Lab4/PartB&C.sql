/*
Using the content of an AdventureWorks database, write a query to list all distinct products included in an order   
for all orders. The report needs to have the following format. Sort the returned data by the sales order id column.   
Within each order, sort the products in the ascending order.
43659
43660
43661
709, 711, 712, 714, 716, 771, 772, 773, 774, 776, 777, 778
758, 762
708, 711, 712, 715, 716, 741, 742, 743, 745, 747, 773, 775, 776, 777, 778
*/

--Part B
--self
WITH temp AS 
	(SELECT DISTINCT 
		SalesOrderID, 
	  ProductID
		FROM Sales.SalesOrderDetail) 
SELECT DISTINCT t2.SalesOrderID, STUFF(
	(SELECT  ', '+RTRIM(CAST(ProductID as char))  
		FROM temp t1 
		WHERE t1.SalesOrderID = t2.SalesOrderID 
		FOR XML PATH('')) , 1, 2, '') AS listProductID
FROM temp t2
ORDER BY SalesOrderID ASC;

--teacher
Select distinct SalesOrderID, 
Stuff((Select ', ' + rtrim(cast(ProductId as char)) 
       From Sales.SalesOrderDetail 
       Where SalesOrderId = h.SalesOrderId
       Order By ProductId
       FOR XML PATH('')) , 1, 2, '') as Products
From Sales.SalesOrderHeader h
Order by h.SalesOrderID

				
--Part C
--self
WITH Parts AS
(
	SELECT 
		b.ProductAssemblyID,
		b.ComponentID,
		b.PerAssemblyQty,
		b.EndDate,
		0 AS ComponentLevel
	FROM Production.BillOfMaterials AS b
	WHERE b.ProductAssemblyID = 992 AND b.EndDate IS NULL
	UNION ALL
	SELECT 
		bom.ProductAssemblyID, 
		bom.ComponentID, 
		p.PerAssemblyQty,
		bom.EndDate,
		ComponentLevel + 1
	FROM Production.BillOfMaterials AS bom
	INNER JOIN Parts AS p
	ON bom.ProductAssemblyID = p.ComponentID AND bom.EndDate IS NULL
),
Temp AS(
	SELECT DISTINCT --should not have DISTINCT here
		p.ComponentID,
		p.ComponentLevel,
		pr.ListPrice,
		RANK() OVER (PARTITION BY p.ComponentLevel ORDER BY pr.ListPrice DESC) AS TopForEachLevel
	FROM Parts AS p
	LEFT JOIN Production.Product AS pr
	ON p.ComponentID = pr.ProductID
)
SELECT
	ComponentLevel,
	ComponentID,
	ListPrice
FROM Temp
WHERE TopForEachLevel=1
ORDER BY ComponentLevel
