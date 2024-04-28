# Write your MySQL query statement below
SELECT B.name AS Department, A.name AS Employee, A.salary AS Salary
FROM Employee A
JOIN Department B ON A.departmentId = B.id
WHERE (A.departmentId,A.salary) IN (
    select departmentId, MAX(salary)
    from Employee
    group by departmentId
)