SELECT
    value AS measurement_value,
    
    coverage__expected_count AS expected_records_in_period,
    coverage__observed_count AS actual_records_observed,
    coverage__expected_interval AS expected_sampling_interval,
    coverage__observed_interval AS actual_sampling_interval,
    coverage__percent_complete AS data_completeness_percent,
    coverage__percent_coverage AS coverage_percent,
    coverage__datetime_from__utc AS coverage_start_utc,
    coverage__datetime_from__local AS coverage_start_local,
    coverage__datetime_to__utc AS coverage_end_utc,
    coverage__datetime_to__local AS coverage_end_local,
    
    period__label AS period_name,
    period__interval AS period_interval,
    period__datetime_from__utc AS period_start_utc,
    period__datetime_from__local AS period_start_local,
    period__datetime_to__utc AS period_end_utc,
    period__datetime_to__local AS period_end_local,
    
    parameter__id AS parameter_id,
    parameter__name AS pollutant_name,
    parameter__units AS measurement_units,
    
    flag_info__has_flags AS has_quality_flags,
    
    _dlt_id AS record_id,
    ETL_LOADED_AT as etl_loaded_at    
FROM {{ source('openaq_dataset_4_resource', 'measurements') }}