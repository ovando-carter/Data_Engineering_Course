-- 1.	Write a query which shows the average share amount for each broker_id rounded to zero decimal places. (this query is not an inline view)

select
    round(avg(share_amount),0) AS "average share amount",
    broker_id
from 
trades
group by broker_id;

--2.	Write a query which shows the lowest average share amount for any broker. 
--HINT: turn the query in question 1 into an inline view and select the lowest number from the average share amount column.

SELECT
            round(avg(share_amount),0) AS "lowest average share amount",
            broker_id
            share_amount
FROM        trades t1
WHERE       share_amount = (SELECT
                                  min(share_amount)
                     FROM         trades t2
                     WHERE        t1.trade_id = t2.trade_id)
Group by broker_id;
                     


--3.	Write a query which shows the average share amount for every broker including those brokers who haven’t made any trades. Your query should return 2 columns: broker name, average share amount.
--HINT: tur query n thefrom question 1 into an inline view and join it to the brokers table.

select  a.average,
        b.first_name||' '||b.last_name as "broker name"
from brokers b
left outer join
(
select
    round(avg(share_amount),0) as average,
    broker_id
from trades
group by broker_id
)a
on a.broker_id = b.broker_id ;





--4.	Write a query which shows the number of trades for each share. (this query is not an inline view)

--5.	Write a query which shows the highest number of trades for any share.
--HINT: turn the query from question 4 into an inline view and select the highest number of trades from it.
