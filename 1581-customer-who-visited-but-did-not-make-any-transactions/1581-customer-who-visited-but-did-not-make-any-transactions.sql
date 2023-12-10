# Write your MySQL query statement below
SELECT A.customer_id, COUNT(*) AS count_no_trans
FROM Visits A
LEFT JOIN Transactions B ON A.visit_id = B.visit_id
WHERE B.transaction_id IS NULL
GROUP BY 1