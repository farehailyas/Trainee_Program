

with source as (

    select * from {{ source('openaq_dataset_4_resource', 'locations__sensors') }}

),

renamed as (

    select
        id,
        name,
        parameter__id,
        parameter__name,
        parameter__units,
        parameter__display_name,
        _dlt_root_id,
        _dlt_parent_id,
        _dlt_list_idx,
        _dlt_id

    from source

)

select * from renamed