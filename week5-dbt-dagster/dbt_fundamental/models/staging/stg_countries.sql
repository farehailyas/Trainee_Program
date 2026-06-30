
with source as (

    select * from {{ source('openaq_dataset_4_resource', 'countries') }}

),

renamed as (

    select
        id as country_id,
        code as country_code,
        name as country_name,
        datetime_first,
        datetime_last,
        _dlt_id as record_id

    from source

)

select * from renamed

