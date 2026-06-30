
with source as (

    select * from {{ source('openaq_dataset_4_resource', 'locations__instruments') }}

),

renamed as (

    select
        id as instrument_id,
        name as instrument_name,
        _dlt_parent_id as location_id,
        _dlt_id as record_id

    from source

)

select * from renamed

