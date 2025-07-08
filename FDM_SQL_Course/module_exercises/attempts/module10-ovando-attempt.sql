-- disply the broker id which made the earliest trade

select 
--    broker_id, 
    min(transaction_time) 
from 
    trades 
--order by 
--    transaction_time ASC
;



SELECT broker_id
FROM   trades
WHERE  transaction_time in 

(
   SELECT min(transaction_time)
   FROM   trades
)
;


-- display the start time with the highest share price for any share

SELECT time_start
FROM   shares_prices
WHERE  price = 

(
   SELECT max(price)
   FROM   shares_prices
)
;