# Write your MySQL query statement below
SELECT name
FROM Employee
WHERE id IN (
    select managerId
    from Employee
    GROUP BY managerId
    HAVING COUNT(managerId) >= 5
)
