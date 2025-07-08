-- Question 1

SELECT broker_id,
       ROUND(AVG(share_amount),0)
FROM   trades
GROUP BY broker_id;


-- Question 2

SELECT MIN(average)
FROM

(
SELECT broker_id,
       ROUND(AVG(share_amount),0) AS average
FROM   trades
GROUP BY broker_id
);


-- Question 3
SELECT b.first_name||' '||b.last_name AS broker, 
       a.average
FROM   brokers b
LEFT OUTER JOIN

(
SELECT broker_id,
       ROUND(AVG(share_amount),0) AS average
FROM   trades
GROUP BY broker_id
)a

ON    a.broker_id = b.broker_id;


-- Question 4

SELECT share_id,
       COUNT(*) AS "Number of trades"
FROM   trades
GROUP BY share_id;


-- Question 5
SELECT MAX(number_of_trades)
FROM
(
SELECT share_id,
       COUNT(*) AS number_of_trades
FROM   trades
GROUP BY share_id
)