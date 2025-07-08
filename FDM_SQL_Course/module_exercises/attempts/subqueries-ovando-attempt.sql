-- 1.	Write a query which shows the names of stock exchanges where some trades have been made.
-- HINT: Use the stock exchanges and trades tables.

select 
name
from 
stock_exchanges 

where stock_ex_id in

(
select
    trade_id
from 
    trades
);



-- 2.	Modify your previous query so that it shows the names of stock exchanges where no trades have been made.

select 
name
from 
stock_exchanges 

where stock_ex_id not in

(
select
    trade_id
from 
    trades
);
-- 3.	Write a query which shows the names of cities which have a stock exchange.
-- HINT: Use the stock exchanges and places tables.
select
    city   
from 
    places
where place_id  in
(
select
    place_id
from 
    stock_exchanges);


-- 4.	Modify your previous query to show cities which don’t have a stock exchange.

select
    city   
from 
    places
where place_id  not in
(
select
    place_id
from 
    stock_exchanges);