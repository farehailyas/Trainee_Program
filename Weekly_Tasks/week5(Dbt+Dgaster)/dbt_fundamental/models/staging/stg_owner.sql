
with source as (

    select * from {{ source('openaq_dataset_4_resource', 'owner') }}

),

renamed as (

    select
        id as owner_id,
        name as owner_name,
        _dlt_id as record_id

    from source

)

select * from renamed
