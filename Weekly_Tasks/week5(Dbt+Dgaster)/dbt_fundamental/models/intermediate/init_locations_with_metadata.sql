{{
    config(
        materialized='incremental',
        incremental_strategy='merge',
        unique_key='location_id'  ,
       
    )
}}
 -- cluster_by=['location_name'],
        -- partition_by=['etl_loaded_at']
   --## partition_by:'col_name' use this for delete+insert strategy which removes a partition n then insert new

-- microbatch
-- event_time='click_timestamp',
--     batch_size='day',
--     begin='2026-01-01',
--     lookback=1
-- on_schema_change = 'fail' to fail model when add/remove new cols in model in incremental strategy

WITH locations AS (
    SELECT location_id, location_name, country_id, owner_id, latitude, longitude, is_mobile,
           record_id, is_active_monitor, etl_loaded_at
    FROM {{ ref('stg_locations') }}
    ORDER BY  etl_loaded_at DESC
),

countries AS (
    SELECT * 
    FROM {{ ref('stg_countries') }}
),

owners AS (
    SELECT *
    FROM {{ ref('stg_owner') }}
),

location_metadata AS (
    SELECT 
        locations.location_id, 
        locations.location_name, 
        locations.country_id, 
        locations.etl_loaded_at,
        countries.country_name, 
        owners.owner_id, 
        owners.owner_name
    FROM locations
    LEFT JOIN countries ON countries.country_id = locations.country_id 
    LEFT JOIN owners ON locations.owner_id = owners.owner_id
)

SELECT lm.*
FROM location_metadata AS lm
{% if is_incremental() %}
    WHERE lm.etl_loaded_at > (SELECT max(etl_loaded_at) FROM {{ this }})
{% endif %}
ORDER BY etl_loaded_at DESC
