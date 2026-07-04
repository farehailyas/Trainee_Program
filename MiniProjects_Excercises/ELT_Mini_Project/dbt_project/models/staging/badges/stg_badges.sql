-- models/staging/stg_badges.sql
with source as (
  select
    badge_id,
    name as badge_name,
    badge_type,
    rank,
    award_count,
    link,
    _dlt_load_id,
    _dlt_id
  from {{ source('raw_stackexchange', 'badges') }}
)
select * from source