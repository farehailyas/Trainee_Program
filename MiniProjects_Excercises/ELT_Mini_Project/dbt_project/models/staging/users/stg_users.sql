-- models/staging/stg_users.sql
with source as (
  select
    user_id,
    account_id,
    display_name,
    reputation,
    user_type,
    is_employee,
    location,
    website_url,
    profile_image as profile_image_url,
    link as profile_link,
    accept_rate,
    badge_counts__bronze as bronze_badge_count,
    badge_counts__silver as silver_badge_count,
    badge_counts__gold as gold_badge_count,
    reputation_change_year,
    reputation_change_quarter,
    reputation_change_month,
    reputation_change_week,
    reputation_change_day,
    TO_TIMESTAMP(creation_date) as created_at,
    TO_TIMESTAMP(last_access_date ) as last_accessed_at,
    TO_TIMESTAMP(last_modified_date ) as last_modified_at,
    _dlt_load_id,
    _dlt_id
  from {{ source('dlt_stack_exchange_source', 'users') }}
)
select * from source