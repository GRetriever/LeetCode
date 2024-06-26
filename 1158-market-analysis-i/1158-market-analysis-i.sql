# Write your MySQL query statement below
SELECT A.user_id AS buyer_id, A.join_date, COUNT(B.buyer_id) AS orders_in_2019
FROM Users A
LEFT JOIN Orders B ON A.user_id = B.buyer_id AND YEAR(B.order_date) LIKE '2019%'
GROUP BY A.user_id