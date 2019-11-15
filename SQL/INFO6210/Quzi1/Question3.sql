-- Question 3 (2 points)
/*
Write a query to retrieve all years which had products of more than 7 unique colors ordered in them.  
For example, in a year if the following products were sold: Product 1 in red, quantity sold 2025
Product 2 in green, quantity sold 3030 Product 3 in yellow, quantity sold 2500 Product 4 in red, quantity sold 1215 Product 5 in green, quantity sold 4050
Then, the sold products had 3 unique colors.  
Exclude the products which don't have a color specified.  
Return the year and the number of the unique colors sold in that year.   
Sort the returned data by the number of unique colors in desc.
*/

-- More than 7 unqiue color -> count for each color group by year -> select when count > 7
with temp as
(
  select year(OrderDate) Year, count(distinct color) Colors
  from Sales.SalesOrderHeader sh
  join Sales.SalesOrderDetail sd
  on sh.SalesOrderID = sd.SalesOrderID
  join Production.Product p
  on sd.ProductID = p.ProductID
  where p.Color is not null
  group by year(OrderDate)
)

select Year, Colors
from temp 
where Colors > 7
order by colors desc;
