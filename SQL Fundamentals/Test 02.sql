-- 1) How many unique transactions are there in the transactions table?
SELECT
  COUNT(DISTINCT transaction_id)

FROM
  grocery_db.transactions;

-- 2) How many customers were in each mailer_type category for the delivery club campaign?

SELECT
  COUNT(customer_id),
  mailer_type
  
FROM
  grocery_db.campaign_data
  
GROUP BY
  mailer_type;


/* 3) Return a list of customers who spent more than $500 and had 5 or more unique transactions in 
the month of August 2020. */

SELECT
  customer_id,
  SUM(sales_cost) AS total_sales,
  COUNT(DISTINCT transaction_id)
  
FROM
  grocery_db.transactions
  
WHERE
  transaction_date BETWEEN '2020-08-01' AND '2020-08-31'
  
GROUP BY
  customer_id
  
HAVING
  SUM(sales_cost) > 500
  AND
  COUNT(DISTINCT transaction_id) >= 5;

-- 4) Return a list of duplicate credit scores that exist in the customer_details table
SELECT
  credit_score, 
  COUNT(credit_score)
  
FROM
  grocery_db.customer_details
  
GROUP BY
  credit_score
  
HAVING
  COUNT(credit_score) > 1;


/* 5) Return the customer_id(s) for the customer(s) who has/have the 2nd highest credit score. Make sure
your code would work for the Nth highest score as well. */ 
CREATE temp TABLE nth_scores AS(
  SELECT
    customer_id,
    credit_score,
    DENSE_RANK() OVER (ORDER BY credit_score DESC) AS highest_score
  
  FROM
    grocery_db.customer_details
  
  WHERE
    credit_score IS NOT NULL
);
  
SELECT
  customer_id,
  highest_score
  
FROM
  nth_scores
  
WHERE
  highest_score = 2;

