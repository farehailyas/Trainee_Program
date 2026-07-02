-- test if measurments have negative value
WITH measurements AS (
    SELECT measurement_value 
    FROM {{ref('stg_measurements')}}
)

SELECT  measurement_value
FROM measurements
WHERE measurement_value < 0