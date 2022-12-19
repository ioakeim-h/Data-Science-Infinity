-- 1) How many rows in the transactions table?
select
  count(*)
  
from
  grocery_db.transactions;
  
-- 2) Return customer id for customer who lives furthest from store
SELECT
  customer_id
  
FROM
  grocery_db.customer_details
  
WHERE
  distance_from_store IN (SELECT MAX(distance_from_store) FROM grocery_db.customer_details);


-- 3) Return number of unique customers in the customer_details table, split by gender
SELECT
  COUNT(DISTINCT customer_id),
  gender
  
FROM
  grocery_db.customer_details
  
GROUP BY
  gender;
  

/* 4) What were the total sales for each product area name for July 2020? Return these in the order of 
highest sales to lowest sales.
*/

CREATE temp TABLE temporary_table AS (
SELECT
  transactions.sales_cost, 
  transactions.transaction_date,
  product_areas.product_area_name

FROM
  grocery_db.transactions INNER JOIN grocery_db.product_areas
  ON transactions.product_area_id = product_areas.product_area_id
  
WHERE
  transactions.transaction_date >= '2020-07-01' AND transactions.transaction_date <= '2020-07-31'
);

SELECT 
  SUM(sales_cost) AS total_sales,
  product_area_name

FROM 
  temporary_table
  
GROUP BY
  product_area_name
  
ORDER BY
  total_sales DESC;


/* 5) Return a list of all customer_id's that do NOT have a loyalty score (i.e. they are in the customer_details
table, but not in the loyalty_scores table)*/
SELECT
  customer_details.customer_id

FROM
  grocery_db.customer_details
  
WHERE
  customer_id NOT IN (SELECT loyalty_scores.customer_id FROM grocery_db.loyalty_scores);

