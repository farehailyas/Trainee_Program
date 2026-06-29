
-- SELECT
--     ID as location_id,
--     NAME as location_name,
--     timezone as timezone_region,
--     is_mobile,
--     IS_MONITOR as is_active_monitor,
--     COORDINATES__LATITUDE as latitude,
--     COORDINATES__LONGITUDE as longitude,
--     COUNTRY__ID as countrty_id,
--     COUNTRY__NAME as country_name,
--     COUNTRY__CODE as country_code,
--     PROVIDER__ID as provider_id,
--     PROVIDER__NAME as provider_name,
--     OWNER__ID as owner_id,
--     OWNER__NAME as owner_name,
--     DATETIME_FIRST__UTC as first_measurement_utc,
--     DATETIME_FIRST__LOCAL first_measurement_local,
--     DATETIME_LAST__UTC as last_measurement_utc,
--     DATETIME_LAST__LOCAL last_measurement_local,
--     locality
-- FROM GITHUB_TO_SNOWFLAKE.DAGSTER_MULTISOURCE.LOCATIONS


SELECT
    location_id,
     location_name,
    timezone_region,
    is_mobile,
    is_active_monitor,
    latitude,
    longitude,
    countrty_id,
    country_name,
    country_code,
    provider_id,
    provider_name,
    owner_id,
    owner_name,
    first_measurement_utc,
    first_measurement_local,
    last_measurement_utc,
    last_measurement_local,
    locality
FROM {{source('DAGSTER_MULTISOURCE' , 'locations')}}
