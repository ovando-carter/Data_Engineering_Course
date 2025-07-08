-- Question 1

SELECT broker_id,
       AVG(price_total) AS avg_price_total
FROM   trades
GROUP BY broker_id;


-- Question 2
SELECT stock_ex_id,
       MIN(transaction_time) AS earliest
FROM   trades
GROUP BY stock_ex_id;


-- Question 3

SELECT currency_id,
       COUNT(share_id) AS number_of_shares
FROM   shares
GROUP BY currency_id;


-- Question 4

SELECT share_id,
       SUM(share_amount) AS total_share_amount
FROM   trades
GROUP BY share_id;


