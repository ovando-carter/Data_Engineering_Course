-- 1.	What currencies are available to price shares in?

select name from currencies;

-- 2.	What trades have been made this month?

select * from trades where to_char(transaction_time, 'yymm') = to_char(sysdate, 'yymm') ;

-- 3.	What companies have their head quarters in New York (place_id 3)?

select name from companies where place_id = 3;

-- 4.	What is the Symbol used for the London Stock Exchange?

select symbol from stock_exchanges where name = 'London Stock Exchange';

-- 5.	What cities are associated with France?

select city from places where country = 'France';

-- 6.	There are two brokers called John, what are their last names?

select last_name from brokers where first_name = 'John';


-- 7.	What trades have been made in the last 7 days?

select * 
from trades 
where to_date(to_char(transaction_time,'DD-MON-YYYY')) > to_date(to_char(sysdate - 7,'DD-MON-YYYY')) ;

-- 8.	List the broker ids who work at the stock exchange id of 1.

select broker_id from broker_stock_ex where stock_ex_id = 1;

-- 9.	Display the company that has a company id of 2.

select company_id from companies where company_id = 2;

-- 10.	 Display the currency that has a currency id of 1.

select name 
from currencies 
where currency_id = 1;

-- 11.	Display the name of the Stock exchange with the symbol TSE.

select name from stock_exchanges where symbol = 'LSE';

-- 12.	Display the last name of the broker whose id is 2.

select last_name from brokers where broker_id = 2;

-- 13.	List the trade ids & price totals of the trades which have taken place at the stock ex id of 3 and share_amount greater than 20000.

select trade_id, price_total 
from trades 
where stock_ex_id = 3 
and share_amount > 20000;

-- 14.	What are the broker ids for the brokers working at stock exchange 2? Sort the broker ids into ascending order.

select * from broker_stock_ex where broker_id = 2;

-- 15.	Which currencies have the word "British" in them?

select * from currencies where name like '%British%';

-- 16.	Which stock exchanges contain "SE" in their symbol. What are their full names? Sort them into descending order.


select * from stock_exchanges where symbol like '%SE%' order by name DESC;


-- 17.	Which share ids have their prices between 400 and 500?

select share_id , price from shares_prices where price between 400 and 500;

-- 18.	Which shares were traded in the last year? (i.e. since this day last year)
-- 19.	Which trade ids took place in this calendar year (i.e. since 1 January)?
-- 20.	Display full details of all trades which took place last year.
-- 21.	Display full details of all trades which took place in the previous quarter.
-- 22.	Which trade ids have had price totals of over 1,000,000 in the last 90 days?
-- 23.	Calculate and display the cost per share for each trade.
