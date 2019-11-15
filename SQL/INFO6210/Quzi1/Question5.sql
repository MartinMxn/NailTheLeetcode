/*
Write a query to retrieve a territory's most valuable order.
The most valuable order has the highest totaldue amount. The totaldue amount is stored in the SalesOrderHeader table. If there is a tie, the tie needs to be retrieved.
Exclude orders that don't a territory specified.
Return the territory's id and name, the order id and totaldue value, and the total order quantity for the order.
Sort the returned data by the territory's id.
*/


with temp as
(select TerritoryID, sh.SalesOrderID, TotalDue,  sum(OrderQty) total,
rank() over (partition by TerritoryID order by TotalDue desc) as ranking
from Sales.SalesOrderHeader sh
join Sales.SalesOrderDetail sd
on sh.SalesOrderID = sd.SalesOrderID
where TerritoryID is not null
group by TerritoryID, sh.SalesOrderID, TotalDue)

select t.TerritoryID, r.Name, t.SalesOrderID, t.TotalDue, t.total
from temp t
join Sales.SalesTerritory r
on t.TerritoryID = r.TerritoryID
where ranking = 1
order by t.TerritoryID;
