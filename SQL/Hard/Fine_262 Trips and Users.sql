SELECT 
    Request_at as Day,
    round((sum(case when Status like 'cancelled%' then 1 else 0 end)
           /
        cast(count(*) as Decimal(9,2))),2) as [Cancellation Rate]
FROM (
    SELECT 
        t.*,
        u1.Banned AS User_ban,
        u2.Banned AS Driver_ban
    FROM Trips AS t
    JOIN Users u1
    ON t.Client_Id = u1.Users_Id
    JOIN Users u2
    ON t.Client_Id = u2.Users_Id
) AS tt
WHERE
    User_ban = 'No' and Driver_ban = 'No'
    and Request_at between '2013-10-01' and '2013-10-03'
GROUP BY Request_at
