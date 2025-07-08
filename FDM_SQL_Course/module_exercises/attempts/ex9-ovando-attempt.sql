-- 1.	Show the average price total for each broker. The results should have two columns: broker_id and average price total.

select 
    broker_id,
    round(avg(price_total),2) as average_price_total 
from 
    trades
group by 
    broker_id ;

-- 2.	Find the date of the earliest trade for each stock exchange. The results should have two columns: stock_ex_id and transaction_time.
select
stock_ex_id,
min(transaction_time) as earliest
from
trades
group by
stock_ex_id;

-- 3.	Show the number of shares priced in each currency. The results should have two columns: currency_id and number of shares priced in that currency.
--this was my attempt - it is incorrect
--select
--    c.currency_id, 
--    sum(t.price_total) as number_of_shares
--From 
--    currencies c
--left outer join
--    shares s
--on 
--    c.currency_id = s.currency_id
--left outer join
    trades t
--on 
--    s.share_id = t.share_id 
--Group by c.currency_id; -- points to what ever is in the select

SELECT currency_id,
       COUNT(share_id) AS number_of_shares
FROM   shares
GROUP BY currency_id;


-- 4.	Show the total share amount for each share. The results should have two columns: share_id and total share amount.
--this was my attempt - it is incorrect
--select
--    s.share_id, 
--    sum(t.share_amount) as total_share_amount
--From 
--    shares s
--left outer join
--    trades t
--on 
--    s.share_id = t.share_id 
--Group by s.share_id; 

SELECT share_id,
       SUM(share_amount) AS total_share_amount
FROM   trades
GROUP BY share_id;
