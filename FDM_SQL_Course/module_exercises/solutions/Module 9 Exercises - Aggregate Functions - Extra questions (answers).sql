-- Question 1

SELECT COUNT(t.trade_id) AS "Number of trades"
FROM   trades t
INNER JOIN 
       stock_exchanges s
ON     s.stock_ex_id = t.stock_ex_id
WHERE  s.symbol = 'NYSE';


-- Question 2

SELECT SUM(t.share_amount) AS "Total traded"
FROM   trades t
INNER JOIN 
       stock_exchanges s
ON     s.stock_ex_id = t.stock_ex_id
WHERE  s.symbol = 'LSE';


-- Question 3

SELECT COUNT(c.name) AS "Number of companies"
FROM   companies c
INNER JOIN 
       places p
ON     p.place_id = c.place_id
WHERE  p.country = 'United Kingdom' AND c.name LIKE 'B%';


-- Question 4

SELECT b.first_name||' '||b.last_name AS broker,
       COUNT(t.trade_id) AS "Number of trades"
FROM   brokers b
INNER JOIN 
       trades t
ON     b.broker_id = t.broker_id
WHERE TO_DATE(TO_CHAR(transaction_time, 'DD-MON-YYYY')) > TO_DATE(TO_CHAR(SYSDATE - 10, 'DD-MON-YYYY'))
--WHERE TO_CHAR(transaction_time, 'YYYYMMDD') > TO_CHAR(SYSDATE - 10, 'YYYYMMDD')
--WHERE TO_NUMBER(TO_CHAR(transaction_time, 'YYYYMMDD')) > TO_NUMBER(TO_CHAR(SYSDATE - 10, 'YYYYMMDD'))
AND    price_total > 1000000
GROUP BY b.first_name||' '||b.last_name;
/* Note: any of the above three conditions would return the correct results, 
   as they compare only the days, months and years (disregarding the time).
   The following condition:
   WHERE  transaction_time > SYSDATE - 10
   is inaccurate as it involves the time as well. Any transactions made on 
   10th day before today later than the time query is ran would also be included.
   Such solution would therefore consider 11 days in the past, rather than just 10.
   In case of transaction_time, the time of transactions is important and it will
   therefore be provided along with the date. There may well be transactions made
   on 10th day before today with the time part later than the time query is ran,
   but these transactions should not be returned.
*/


-- Question 5

SELECT c.name,
       SUM(t.share_amount) AS "Total share amount"
FROM   companies c
INNER JOIN
       shares s
ON     c.company_id = s.company_id
INNER JOIN
       trades t
ON     t.share_id = s.share_id
WHERE TO_DATE(TO_CHAR(transaction_time, 'DD-MON-YYYY')) > TO_DATE(TO_CHAR(SYSDATE - 90, 'DD-MON-YYYY'))
--WHERE TO_CHAR(transaction_time, 'YYYYMMDD') > TO_CHAR(SYSDATE - 90, 'YYYYMMDD')
--WHERE TO_NUMBER(TO_CHAR(transaction_time, 'YYYYMMDD')) > TO_NUMBER(TO_CHAR(SYSDATE - 90, 'YYYYMMDD'))
GROUP BY c.name;
/* Note: any of the above three conditions would return the correct results, 
   as they compare only the days, months and years (disregarding the time),
   but the following one would include the time element when comparing dates:
   WHERE  transaction_time > SYSDATE - 90
   This may cause a different output, as it will consider records with the date 
   90th day ago having the time part later than the time the query is ran. Note 
   that the date 90th day ago is 91th day from today (as today's date is included).
*/


-- Question 6

SELECT p.city,
       COUNT(c.company_id) AS "Number of companies"
FROM   places p
INNER JOIN
       companies c
ON     p.place_id = c.place_id
GROUP BY p.city;


-- Question 7

SELECT c.name,
       ROUND(AVG(t.price_total),0) AS "Average price total"
FROM   companies c
INNER JOIN
       shares s
ON     s.company_id = c.company_id
INNER JOIN
       trades t
ON     t.share_id = s.share_id
GROUP BY c.name;


-- Question 8

SELECT b.first_name||' '||b.last_name AS broker,
       COUNT(bs.stock_ex_id) AS "Number of exchanges"
FROM   brokers b
INNER JOIN 
       broker_stock_ex bs
ON     b.broker_id = bs.broker_id
GROUP BY b.first_name||' '||b.last_name;


-- Question 9

SELECT c.name,
       COUNT(s.share_id) AS "Number of shares"
FROM   currencies c
INNER JOIN
       shares s
ON     s.currency_id = c.currency_id
GROUP BY c.name;


-- Question 10

SELECT c.name,
       TO_CHAR(sp.time_start,'MM') AS month,
       ROUND(AVG(sp.price),2) AS "Average share price"
FROM   companies c
INNER JOIN 
       shares s
ON     s.company_id = c.company_id
INNER JOIN
       shares_prices sp
ON     sp.share_id = s.share_id
GROUP BY c.name, TO_CHAR(sp.time_start,'MM')
ORDER BY c.name, TO_CHAR(sp.time_start,'MM');