
WITH locations AS (
    SELECT location_id, location_name ,country_id ,owner_id , latitude , longitude , record_id ,is_active_monitor 
    FROM {{ref('stg_locations')}}
),
instruments AS (
    SELECT *
    FROM {{ref('stg_location_instruments')}}
),

sensors AS (
    SELECT *
    FROM {{ref('stg_location_sensors')}}
),


instruments_counts AS (
    SELECT locations.location_id, COUNT(DISTINCT instruments.instrument_id) as instruments_count
    FROM locations
    LEFT JOIN instruments
    ON locations.record_id = instruments.location_id
    GROUP BY locations.location_id
),

sensors_counts AS (
    SELECT locations.location_id, COUNT(DISTINCT sensors.sensor_id) as sensors_count 
    FROM locations
    LEFT JOIN sensors
    ON locations.record_id = sensors.location_id
    WHERE locations.is_active_monitor = TRUE
    GROUP BY locations.location_id
  
)
,
locations_stats AS(
    SELECT instruments_counts.location_id ,  instruments_counts.instruments_count , sensors_counts.sensors_count 
    FROM instruments_counts 
    LEFT JOIN sensors_counts
    ON instruments_counts.location_id = sensors_counts.location_id
)

SELECT *
FROM locations_stats
