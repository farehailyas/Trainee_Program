-- models/staging/stg_tags__collectives.sql
with source as (
  select
    name as collective_name,
    slug as collective_slug,
    description,
    link,
    _dlt_root_id as tag_id,
    _dlt_parent_id,
    _dlt_list_idx as list_index,
    _dlt_id
  from {{ source('dlt_stack_exchange_source', 'tags__collectives') }}
)
select * from source