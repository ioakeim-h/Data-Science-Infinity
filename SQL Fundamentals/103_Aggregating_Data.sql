-- AGGREGATING DATA
--------------------------------------------------------------------

-- AGGREGATION FUNCTIONS
SELECT
  SUM(sales_cost) AS total_sales, 
  AVG(sales_cost) AS avg_sales,
  MIN(sales_cost) AS min_sales,
  MAX(sales_cost) AS max_sales,
  COUNT(*) AS num_rows,
  COUNT (DISTINCT transaction_id) AS num_transactions
  
  
FROM
  grocery_db.transactions;

-- THE GROUP BY STATEMENT
SELECT
  transaction_date,
  SUM(sales_cost) AS total_sales,
  SUM(num_items) AS total_items,
  COUNT (DISTINCT transaction_id) AS num_transactions
  
FROM
  grocery_db.transactions
  
GROUP BY
  transaction_date
  
ORDER BY
  transaction_date;

-- GROUPING BY MULTIPLE VARIABLES
SELECT
  product_area_id,
  transaction_date,
  SUM(sales_cost) AS total_sales,
  SUM(num_items) AS total_items,
  COUNT (DISTINCT transaction_id) AS num_transactions
  
FROM
  grocery_db.transactions
  
GROUP BY
  product_area_id,
  transaction_date
  
ORDER BY
  product_area_id,
  transaction_date;

-- THE HAVING CLAUSE
SELECT
  product_area_id,
  SUM(sales_cost) AS total_sales
  
FROM
  grocery_db.transactions
  
GROUP BY
  product_area_id
  
HAVING
  SUM(sales_cost) > 200000;
