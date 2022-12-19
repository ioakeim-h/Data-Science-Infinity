-- USEFUL TIPS & TRICKS (VOLUME 1)
-----------------------------------------------------------------------------------

-- Using Sub-Queries
select
  product_area_name,
  profit_margin
  
from
  grocery_db.product_areas
  
where
  --profit_margin = (select max(profit_margin) from grocery_db.product_areas)
  profit_margin = (select profit_margin from grocery_db.product_areas order by profit_margin desc limit 1);


-- Using Lead & Lag




-- Rounding Data



-- Random Sampling
