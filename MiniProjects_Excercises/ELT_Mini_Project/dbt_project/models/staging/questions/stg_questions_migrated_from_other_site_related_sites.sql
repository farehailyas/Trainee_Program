-- models/staging/stg_questions__migrated_from__other_site__related_sites.sql
with source as (
  select
    name as related_site_name,
    relation as site_relation,
    site_url,
    api_site_parameter,
    _dlt_root_id as question_id,
    _dlt_parent_id,
    _dlt_list_idx as list_index,
    _dlt_id
  from {{ source('raw_stackexchange', 'questions__migrated_from__other_site__related_sites') }}
)
select * from source