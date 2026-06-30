WITH measurements AS(
    SELECT *
    FROM {{ref('stg_measurements')}}

)
SELECT * FROM measurements