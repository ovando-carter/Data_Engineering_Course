--- 1.	List broker IDs which have an average price total of over 4,000,000
--- HINT: modify your query from module 9 part 1.
  
SELECT broker_id
FROM   trades
GROUP BY broker_id
HAVING AVG(price_total) > 4000000;

--- 2.	List stock exchange IDs where each stock exchange’s earliest transaction time took place within the last 365 days.
--- HINT: modify your query from module 9 part 2.

select
stock_ex_id
from trades
group by stock_ex_id
having min(transaction_time) > add_months(sysdate, - 12);



--- 3.	List currency IDs used to price 4 or more shares.
--- HINT: modify your query from module 9 part 3.

select currency_id
from shares
group by currency_id
having count(share_id)>=4;


--- 4.	List share IDs with a total share amount above 100,000
--- HINT: modify your query from module 9 part 4.

select share_id
from trades
group by share_id
having sum(share_amount) > 100000;

--- 5.	List place IDs with more than 2 companies.
--- HINT: find the number of companies for each place ID and then filter your results.

select place_id
from companies
group by place_id
having count(name)>2; -- they have *, why? 

--- 6.	List share IDs whose highest price total is above 1 million.
--- HINT: find the highest price total for each share ID and then filter your results.

select share_id
from trades
group by share_id
having max(price_total) > 1000000;

--- 7.	List share IDs which have been traded more than twice by broker ID 1.
--- HINT: use WHERE and HAVING

select share_id
from trades
where broker_id = 1
group by share_id
having count(*)>2; -- why is this not count(trade_id)?

--- 8.	List share IDs which have more than 5 trades with a price_total above 1 million.
--- HINT: use WHERE and HAVING

select share_id
from trades
where price_total > 1000000
group by share_id
having count(trade_id) > 5
