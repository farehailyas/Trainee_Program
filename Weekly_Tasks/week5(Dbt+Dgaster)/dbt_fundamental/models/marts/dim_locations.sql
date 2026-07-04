WITH locations_metadata AS(
    SELECT *
    FROM {{ref('init_locations_with_metadata')}}
),

locations_stats AS (
    SELECT *
    FROM {{ref('init_locations_stats')}}
),

locations_metadata_with_stats AS (
    SELECT locations_metadata.* ,  locations_stats.instruments_count , locations_stats.sensors_count 
    FROM locations_metadata
    LEFT JOIN locations_stats
    ON locations_metadata.location_id = locations_stats.location_id
)
SELECT *
FROM locations_metadata_with_stats
