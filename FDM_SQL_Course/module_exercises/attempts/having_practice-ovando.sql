-- list share_id with average share price less than 100
select share_id
from shares_prices
group by share_id
having round(avg(price),2)<100;

-- list broker_ids where trades are greater then 10
select broker_id
from trades
group by broker_id
having count(trade_id)>=10;
