CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
    RETURN (
        select DISTINCT salary
        from Employee
        order by salary DESC
        limit 1 OFFSET N
    );
END