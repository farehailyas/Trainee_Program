-- models/staging/stg_answers__posted_by_collectives__tags.sql
with source as (
  select
    value as tag_value,
    _dlt_root_id as answer_id,
    _dlt_parent_id,
    _dlt_list_idx as list_index,
    _dlt_id
  from {{ source('raw_stackexchange', 'answers__posted_by_collectives__tags') }}
)
select * from source