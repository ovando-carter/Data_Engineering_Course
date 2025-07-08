-- Question 1
SELECT name
FROM   currencies;


-- Question 2
SELECT trade_id,
       share_id,
       broker_id,
       stock_ex_id,
       transaction_time,
       share_amount,
       price_total
FROM   trades 
WHERE  TO_CHAR(transaction_time,'YYMM') = TO_CHAR(SYSDATE,'YYMM');


-- Question 3
SELECT name
FROM   companies
WHERE  place_id = 3;


-- Question 4
SELECT symbol
FROM   stock_exchanges
WHERE  name = 'London Stock Exchange';


-- Question 5
SELECT city
FROM   places
WHERE  country = 'France';


-- Question 6
SELECT last_name
FROM   brokers
WHERE  first_name = 'John';


-- Question 7
-- Option 1: compare day, month and year part of dates, as dates
SELECT trade_id,
       share_id,
       broker_id,
       stock_ex_id,
       transaction_time,
       share_amount,
       price_total
FROM   trades 
WHERE TO_DATE(TO_CHAR(transaction_time, 'DD-MON-YYYY')) > TO_DATE(TO_CHAR(SYSDATE - 7, 'DD-MON-YYYY'))
;
-- Option 2: compare day, month and year part of dates, as characters
SELECT trade_id,
       share_id,
       broker_id,
       stock_ex_id,
       transaction_time,
       share_amount,
       price_total
FROM   trades 
WHERE TO_CHAR(transaction_time, 'YYYYMMDD') > TO_CHAR(SYSDATE - 7, 'YYYYMMDD')
;
-- Option 3: compare day, month and year part of dates, as numbers
SELECT trade_id,
       share_id,
       broker_id,
       stock_ex_id,
       transaction_time,
       share_amount,
       price_total
FROM   trades 
WHERE TO_NUMBER(TO_CHAR(transaction_time, 'YYYYMMDD')) > TO_NUMBER(TO_CHAR(SYSDATE - 7, 'YYYYMMDD'))
;
/* Any of the above 3 options compare only the year, month and day (disregarding the time), which is correct.
   Note: the following condition:
   WHERE  transaction_time > SYSDATE - 7;
   compares the two dates including the time element (up to and including the seconds).
   It would therefore retrieve any trade made 7 days ago at a time later than the time the query was ran.
   In this case, records are dynamically created; therefore the time of running queries will
   always be later than the time records were stored - consequently, you can't see the difference.
   In reality, records are not created dynamically - they will have a specific time that may be
   before or after the time the query is ran. The above condition will include any record
   created 7 days ago that has the time element later than the time the query was ran.
*/


-- Question 8

SELECT broker_id
FROM   broker_stock_ex
WHERE  stock_ex_id = 1;


-- Question 9

SELECT name
FROM   companies
WHERE  company_id = 2;


-- Question 10

SELECT name 
FROM   currencies
WHERE currency_id = 1;


-- Question 11

SELECT name
FROM   stock_exchanges 
WHERE  symbol = 'TSE';


-- Question 12

SELECT first_name,
       last_name
FROM   brokers 
WHERE  broker_id = 2;


-- Question 13

SELECT trade_id,
       price_total
FROM   trades
WHERE  stock_ex_id = 3
AND    share_amount > 20000;


-- Question 14

SELECT broker_id
FROM   broker_stock_ex
WHERE  stock_ex_id = 2
ORDER BY broker_id;


-- Question 15

SELECT name
FROM   currencies
WHERE  name LIKE '%British%';


-- Question 16

SELECT name
FROM   stock_exchanges
WHERE  symbol LIKE '%SE%'
ORDER BY name DESC;


-- Question 17

SELECT DISTINCT share_id
FROM   shares_prices
WHERE  price >= 400 AND price <= 500;


-- Question 18

SELECT DISTINCT share_id
FROM   trades
WHERE  TO_CHAR(transaction_time,'YYMMDD') > TO_CHAR(ADD_MONTHS(SYSDATE,-12),'YYMMDD');

/* Note: the following query 
        SELECT DISTINCT share_id
        FROM   trades
        WHERE  transaction_time > ADD_MONTHS(SYSDATE,-12);
   is not a correct solution because the time the query
   is ran will have an impact on the retrieved records: it will return all trades
   made on dates greater than today last year (which is correct), but will also possibly
   include some trades made on date equal to today last year (which is incorrect). 
   ADD_MONTHS(SYSDATE,-12) returns the current day (DD), curent month(MM), last year (YYYY-1) 
   and same time as the time of running the query.
   Oracle then compares the values in transaction_time column (up to and including the seconds)
   to the date & time returned by ADD_MONTHS(SYSDATE,-12). Trades made in the current date a year ago 
   with times later than the time when the query was run will be returned, which is wrong, as we
   need to retrieve all records since, but not on, this day last year.
   For example if the query was ran at on 10/11/2021 at 14:20:30 and there were two trades on 
   10/11/2020: one at 14:00:00 and another on 14:30:00, the query will not return the first one 
   but will return the second one.
   The correct solution needs to return none of the two trades, since the comparison operator is >
   (none of the trades made on 10/11/2020 should be returned; only the trades made on 11/11/2020 
   and later should be returned).
   If the comparison operator was >=, the correct solution needs to return both of these two trades
   (all trades made on 10/11/2020 should also be returned).
*/

SELECT DISTINCT share_id
FROM   trades
WHERE  transaction_time > ADD_MONTHS(SYSDATE,-12);

SELECT TO_CHAR(ADD_MONTHS(SYSDATE,-12),'YYYYMMDD HH24:MI:SS')
FROM dual;

-- Question 19

SELECT trade_id
FROM   trades
WHERE  TO_CHAR(transaction_time,'YY') = TO_CHAR(SYSDATE,'YY');


-- Question 20

SELECT *
FROM trades
WHERE  TO_CHAR(transaction_time,'YY') = TO_CHAR(ADD_MONTHS(SYSDATE,-12),'YY');


-- Question 21

SELECT *
FROM trades
WHERE  TO_CHAR(transaction_time,'QYY') = TO_CHAR(ADD_MONTHS(SYSDATE,-3),'QYY');


-- Question 22

SELECT trade_id 
FROM   trades
WHERE TO_DATE(TO_CHAR(transaction_time, 'DD-MON-YYYY')) > TO_DATE(TO_CHAR(SYSDATE - 90, 'DD-MON-YYYY'))
--WHERE TO_CHAR(transaction_time, 'YYYYMMDD') > TO_CHAR(SYSDATE - 90, 'YYYYMMDD')
--WHERE TO_NUMBER(TO_CHAR(transaction_time, 'YYYYMMDD')) > TO_NUMBER(TO_CHAR(SYSDATE - 90, 'YYYYMMDD'))
AND    price_total > 1000000;
/* Note: any of the above three conditions would return the correct results, 
   as they compare only the days, months and years (disregarding the time).
   The following condition:
   WHERE  transaction_time > SYSDATE - 90
   is inaccurate as it involves the time as well. Any transactions made on 
   90th day before today later than the time query is ran would also be included.
   Such solution would therefore consider 91 days in the past, rather than just 90.
   In case of transaction_time, the time of transactions is important and it will
   therefore be provided along with the date. There may well be transactions made
   on 90th day before today with the time part later than the time query is ran,
   but these transactions should not be returned.
*/

-- Question 23

SELECT trade_id,
       price_total / share_amount
FROM   trades; 