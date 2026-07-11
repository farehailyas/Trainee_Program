-- models/staging/stg_tags.sql
with source as (
  select
    name as tag_name,
    count as tag_count,
    is_moderator_only,
    is_required,
    has_synonyms,
    _dlt_load_id,
    _dlt_id
  from {{ source('dlt_stack_exchange_source', 'tags') }}
)
select * from source