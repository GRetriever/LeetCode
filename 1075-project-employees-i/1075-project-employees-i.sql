# Write your MySQL query statement below
SELECT A.project_id, ROUND(AVG(B.experience_years),2) AS average_years
FROM Project A
JOIN Employee B ON A.employee_id = B.employee_id
GROUP BY project_id