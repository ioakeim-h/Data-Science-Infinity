/* 1) Return a list of customers from the loyalty_scores table who have a customer_loyalty_score of 
0.77, 0.88, or 0.99 */

SELECT
  customer_id,
  customer_loyalty_score
  
FROM
  grocery_db.loyalty_scores
  
WHERE
  customer_loyalty_score IN (0.77, 0.88, 0.99);
  
-- 2) Return the average customer_loyalty_score for customers, split by gender.

SELECT
  AVG(loyalty_scores.customer_loyalty_score) AS avg_loyalty_score,
  customer_details.gender
  
FROM
  grocery_db.loyalty_scores INNER JOIN grocery_db.customer_details 
    ON loyalty_scores.customer_id = customer_details.customer_id
    
GROUP BY
  gender;

/* 3) Return customer_id, distance_from_store, and a new column called distance_category that tags customers 
who are less than 1 mile from store as "Walking Distance", 1 mile or more from store as "Driving Distance" 
and "Unknown" for customers where we do not know their distance from the store. */

SELECT
  customer_id,
  distance_from_store,
  CASE
    WHEN distance_from_store < 1 THEN 'Walking Distance'
    WHEN distance_from_store > 1 THEN 'Driving Distance'
    ELSE 'Unknown' 
    END AS detailed_distance
   
FROM
  grocery_db.customer_details;


/* 4) For the 400 customers with a customer_loyalty_score, divide them up into 10 deciles, and calculate 
the average distance_from_store for each decile. */

WITH loyalties_distance AS(
  SELECT
    loyalty_scores.customer_id,
    loyalty_scores.customer_loyalty_score,
    ntile(10) over (order by loyalty_scores.customer_loyalty_score desc) as loyalty_category,
    customer_details.distance_from_store
  
  FROM
    grocery_db.loyalty_scores INNER JOIN grocery_db.customer_details
      ON loyalty_scores.customer_id = customer_details.customer_id
    
)

SELECT
  loyalty_category,
  AVG(distance_from_store) AS avg_store_distance
  
FROM
  loyalties_distance
  
GROUP BY
  loyalty_category;

/* 5) Return data showing, for each product_area_name - the total sales, and the percentage of overall sales
that each product area makes up. */

SELECT
  product_areas.product_area_name,
  SUM(transactions.sales_cost) AS total_sales,
  SUM(transactions.sales_cost) * 100 / SUM(SUM(transactions.sales_cost)) OVER () AS sales_percentage

FROM
  grocery_db.product_areas INNER JOIN grocery_db.transactions 
    ON product_areas.product_area_id = transactions.product_area_id
    
GROUP BY
  product_areas.product_area_name;
