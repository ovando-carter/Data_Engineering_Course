-- Question 1

SELECT broker_id
FROM   trades
GROUP BY broker_id
HAVING AVG(price_total) > 4000000;


-- Question 2
SELECT stock_ex_id
FROM   trades
GROUP BY stock_ex_id
HAVING MIN(transaction_time) > ADD_MONTHS(SYSDATE,-12);


-- Question 3

SELECT currency_id
FROM   shares
GROUP BY currency_id
HAVING COUNT(share_id) >=4;


-- Question 4

SELECT share_id
FROM   trades
GROUP BY share_id
HAVING SUM(share_amount) > 100000;

-- Question 5

SELECT place_id
FROM   companies
GROUP BY place_id
HAVING COUNT(*) > 2;

-- Question 6
SELECT share_id
FROM   trades
GROUP BY share_id
HAVING MAX(price_total) > 1000000;


-- Question 7

SELECT share_id
FROM   trades
WHERE  broker_id = 1
GROUP BY share_id
HAVING COUNT(*) > 2;


-- Question 8

SELECT share_id
FROM   trades
WHERE  price_total > 1000000
GROUP BY share_id
HAVING COUNT(trade_id) > 5;






