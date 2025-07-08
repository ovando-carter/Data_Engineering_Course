-- ovando attempt
-- Q1 Create a list of companies and their locations. The results should have three columns - company name, city & country.
select 
    name, country, city
from 
    companies c     
join 
    places p 
on
    c.place_id = p.place_id;

-- Q2 Create a list of the companies and the stock exchanges they’re traded on. The results should show company name and stock exchange name.
-- HINT: join the companies table directly to the stock exchange table

select 
    c.name AS company_name, s.name AS stock_exchange_name
from
    companies c
join
    stock_exchanges s
on 
    c.place_id = s.place_id;
    
-- Q3 Create a list of shares and the currencies they’re priced in. The results should have two columns – share_id and currency name.
select
    share_id, c.name AS currency_name
from 
    shares s
left join
    currencies c
on 
    s.currency_id = c.currency_id;

-- Q4 Create a list of all currency names and any shares they’re used to price. 
-- The list should include currencies which are not used to price any share. 
-- The results should show two columns: currency name and share_id.
-- HINT: modify your query from question 3 to use an outer join.
select
    share_id, c.name AS currency_name
from 
    shares s
left join
    currencies c 
on 
    s.currency_id = c.currency_id;

-- Q5  Find the name of any currencies that are not used to price any share.
-- HINT: modify your query from question 4 to use a filter.
-- how is this different from Q4
select
    share_id, c.name AS currency_name
from 
    shares s
full outer join
    currencies c 
on 
    s.currency_id = c.currency_id
where 
    share_id is null;
    
-- Q6 Write a query that will give you the name of each company and the name of the currency their shares are traded in.
-- HINT: join 3 tables – companies, shares and currencies

select
    a.name AS Compant_Name,   
    c.name AS Currency
from 
    companies a
Inner Join
    shares s
on 
    a.company_id = s.company_id
Inner Join
    currencies c
on 
    s.currency_id = c.currency_id;



-- Q7 Create a list of the brokers with the stock exchanges assigned to them. The results should have two columns – broker’s name & stock exchange name. 
-- HINT: join 3 tables – brokers, broker_stock_ex and stock_exchanges.

SELECT b.first_name||' '||b.last_name AS broker,
       s.name
FROM   brokers b
INNER JOIN
       broker_stock_ex bse
ON b.broker_id = bse.broker_id
INNER JOIN
       stock_exchanges s
ON bse.stock_ex_id = s.stock_ex_id;

