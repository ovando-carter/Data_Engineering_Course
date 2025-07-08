
--Display broker ids with the number of different shares traded by each broker id/*SELECT DISTINCT
broker_id,
share_id
FROM trades;
*/
--NB The COUNT counts the number of rows retrned by the inline view so could use broker_id or *SELECT broker_id,
COUNT(share_id) AS "No of Different Shares"
FROM (SELECT DISTINCT broker_id,
share_id
FROM trades)
GROUP BY broker_id
ORDER BY broker_id;


-- Display broke ids with the number of different stock exchanges they traded in by each broker id
select
count(stock_ex_id) AS "No of Different Stock Exchange",
broker_id
from (select distinct stock_ex_id,
broker_id
from trades)
group by broker_id
order by broker_id;


-- Display share with the number of different stock exchanges where share was traded for each
select
count(stock_ex_id) AS "no of different stock exchange",
share_id
from (select distinct stock_ex_id,
share_id
from trades)
group by share_id
order by share_id;