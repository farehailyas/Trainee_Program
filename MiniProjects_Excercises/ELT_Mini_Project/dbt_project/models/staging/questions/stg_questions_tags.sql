-- models/staging/stg_answers__posted_by_collectives__tags.sql
with source as (
  select
    value as tag_value,
    _dlt_root_id as question_id,
    _dlt_parent_id,
    _dlt_list_idx as list_index,
    _dlt_id as tag_id
   
  from {{ source('dlt_stack_exchange_source', 'questions__tags') }}
)
select * from source