-- THE BASIC SELECT STATEMENT
-------------------------------------------------------------------------

-- THE SELECT STATEMENT
SELECT 
  *

FROM
  grocery_db.product_areas


-- LIMIT
SELECT 
  *

FROM
  grocery_db.product_areas

LIMIT
  3;


-- ORDER BY
SELECT 
  *

FROM
  grocery_db.customer_details

ORDER BY 
  distance_from_store,
  credit_score;


-- DISTINCT
SELECT
  DISTINCT
  *
  
FROM
  grocery_db.customer_details;
  

-- GIVING COLUMNS AN ALIAS
SELECT
  distance_from_store AS distance_to_store,
  customer_id AS customer_number
  
FROM
  grocery_db.customer_details;
  

-- CREATING NEW COLUMNS
SELECT
  distance_from_store AS distance_to_store,
  customer_id AS customer_number,
  1 AS new_col,
  distance_from_store * 1.6 AS distance_from_store_km
  
FROM
  grocery_db.customer_details;
