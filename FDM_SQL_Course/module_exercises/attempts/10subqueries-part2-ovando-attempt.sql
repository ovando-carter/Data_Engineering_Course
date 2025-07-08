-- 1.	Show the stock_ex_id of the stock exchange where the most recent trade took place.
-- HINT: start by finding the date of the most recent trade


select 
stock_ex_id
from 
trades
where transaction_time = 

(select 
max(transaction_time)
from 
trades);



-- 2.	Show the broker_id of the broker who made the trade with the highest trade_id.
select 
broker_id
from 
trades
where trade_id =
(select
max(trade_id)
from 
trades);


-- 3.	List the trade_ids which have an above average share_amount.

select
trade_id
from trades
where share_amount >
(select
avg(share_amount)
from 
trades
);