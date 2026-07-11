-- models/staging/stg_users__collectives.sql
with source as (
  select
    role as user_collective_role,
    collective__name as collective_name,
    collective__slug as collective_slug,
    collective__description,
    collective__link,
    _dlt_root_id as user_id,
    _dlt_parent_id,
    _dlt_list_idx as list_index,
    _dlt_id
  from {{ source('dlt_stack_exchange_source', 'users__collectives') }}
)
select * from source