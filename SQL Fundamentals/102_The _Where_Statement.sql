-- PART 2: APPLYING SELECTION CONDITIONS USING THE WHERE STATEMENT
-----------------------------------------------------------------------------------

-- THE WHERE STATEMENT
SELECT 
  *
  
FROM
  grocery_db.customer_details
  
WHERE
  distance_from_store < 2;

-- MULTIPLE CONDITIONS

-- AND
SELECT 
  *
  
FROM
  grocery_db.customer_details
  
WHERE
  distance_from_store < 2 AND
  gender = 'M';

-- OR
SELECT 
  *
  
FROM
  grocery_db.customer_details
  
WHERE
  distance_from_store < 2 OR
  gender = 'M';

-- OTHER OPERATORS

/*
Equal to =
Not equal to <>
Greater than/Less than/Equal < > <=
*/

SELECT
  * 
  
FROM
  grocery_db.campaign_data;


-- IN
SELECT
  * 
  
FROM
  grocery_db.campaign_data
  
WHERE
  mailer_type IN ('Mailer1','Mailer2');

-- LIKE
SELECT
  * 
  
FROM
  grocery_db.campaign_data
  
WHERE
  mailer_type LIKE 'Mailer%';
