-- models/staging/stg_users__collectives__collective__tags.sql
with source as (
  select
    value as collective_tag,
    _dlt_root_id as user_id,
    _dlt_parent_id,
    _dlt_list_idx as list_index,
    _dlt_id
  from {{ source('dlt_stack_exchange_source', 'users__collectives__collective__tags') }}
)
select * from source