-- models/staging/stg_users__collectives__collective__external_links.sql
with source as (
  select
    type as link_type,
    link as external_link,
    _dlt_root_id as user_id,
    _dlt_parent_id,
    _dlt_list_idx as list_index,
    _dlt_id
  from {{ source('dlt_stack_exchange_source', 'users__collectives__collective__external_links') }}
)
select * from source