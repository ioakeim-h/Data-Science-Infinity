-- UNION & UNION ALL
----------------------------------------------------------------------------------

select product_area_name from grocery_db.product_areas where product_area_id in (1,2)
union
select product_area_name from grocery_db.product_areas where product_area_id in (4,5);


select product_area_name from grocery_db.product_areas where product_area_id in (1,2)
union all
select product_area_name from grocery_db.product_areas where product_area_id in (1,2)
union all
select product_area_name from grocery_db.product_areas where product_area_id in (1,2);
