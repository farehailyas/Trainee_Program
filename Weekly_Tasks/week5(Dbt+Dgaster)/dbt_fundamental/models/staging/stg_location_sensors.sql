

with source as (

    select * from {{ source('openaq_dataset_4_resource', 'locations__sensors') }}

),

renamed as (

    select
        id as sensor_id,
        name as sensor_name,
        parameter__id as parameter_id ,
        parameter__name as parameter_name,
        parameter__units as parameter_unit,
        parameter__display_name as parameter_display_name,
        _dlt_parent_id as location_id,
        _dlt_id as record_id

    from source

)

select * from renamed