-- Question 1

SELECT b.first_name||' '||b.last_name AS broker
FROM   brokers b
INNER JOIN
       broker_stock_ex bs
ON     b.broker_id = bs.broker_id
WHERE  bs.stock_ex_id = 1;


-- Question 2

SELECT b.first_name||' '||b.last_name AS broker
FROM   brokers b
INNER JOIN
       broker_stock_ex bs
ON     b.broker_id = bs.broker_id
INNER JOIN 
       stock_exchanges s
ON     s.stock_ex_id = bs.stock_ex_id
WHERE  s.symbol = 'NYSE';


-- Question 3

SELECT c.name
FROM   companies c
INNER JOIN
       places p
ON     p.place_id = c.place_id
WHERE  p.city = 'London';


-- Question 4

SELECT p.city
FROM   companies c
RIGHT OUTER JOIN
       places p
ON     p.place_id = c.place_id
WHERE  c.company_id IS NULL;


-- Question 5

SELECT c.name AS company,
       cu.name AS currency
FROM   companies c
INNER JOIN
       shares s
ON     c.company_id = s.company_id
INNER JOIN
       currencies cu
ON     cu.currency_id = s.currency_id;


-- Question 6

SELECT b.first_name||' '||b.last_name AS broker
FROM   brokers b
INNER JOIN 
       broker_stock_ex bs
ON     b.broker_id = bs.broker_id
INNER JOIN
       stock_exchanges s
ON     s.stock_ex_id = bs.stock_ex_id
INNER JOIN
       places p
ON     p.place_id = s.place_id
WHERE  p.country = 'United Kingdom';


-- Question 7

SELECT t.trade_id,
       sp.price * t.share_amount AS "Base Price Total"
FROM trades t
   INNER JOIN
     shares s
   ON s.share_id = t.share_id
   INNER JOIN
     shares_prices sp
   ON sp.share_id = s.share_id
WHERE sp.time_end IS NOT NULL
AND t.transaction_time BETWEEN sp.time_start AND sp.time_end  -- this and the previous condition together identify past shares' prices
OR sp.time_end IS NULL
AND t.transaction_time >= sp.time_start  -- this and the previous condition together identify current shares' prices
ORDER BY t.trade_id;


-- Question 8

SELECT t.trade_id,
       sp.price * t.share_amount AS "Base Price Total",
       sp.price * t.share_amount * 0.025 AS "Commission",
       sp.price * t.share_amount * (1 + 0.025) AS "Overall Price Total"
FROM trades t
   INNER JOIN
     shares s
   ON s.share_id = t.share_id
   INNER JOIN
     shares_prices sp
   ON sp.share_id = s.share_id
WHERE sp.time_end IS NOT NULL
AND t.transaction_time BETWEEN sp.time_start AND sp.time_end
OR sp.time_end IS NULL
AND t.transaction_time >= sp.time_start
ORDER BY t.trade_id;

/* Note: in reality shares change their prices very often (as often 
   as every second). In order to work out the price of a share at
   any moment in time, both date & time parts of transaction_time, 
   time_start and time_end must be considered. Since in case of 
   questions 7 and 8 time matters, TO_CHAR should not be used.
*/