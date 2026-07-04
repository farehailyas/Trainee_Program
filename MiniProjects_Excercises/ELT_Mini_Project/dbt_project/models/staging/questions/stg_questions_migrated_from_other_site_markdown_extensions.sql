-- models/staging/stg_questions__migrated_from__other_site__markdown_extensions.sql
with source as (
  select
    value as markdown_extension,
    _dlt_root_id as question_id,
    _dlt_parent_id,
    _dlt_list_idx as list_index,
    _dlt_id
  from {{ source('raw_stackexchange', 'questions__migrated_from__other_site__markdown_extensions') }}
)
select * from source