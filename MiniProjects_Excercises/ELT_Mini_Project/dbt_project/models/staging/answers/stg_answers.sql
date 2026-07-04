-- models/staging/stg_answers.sql
with source as (
  select
    answer_id,
    question_id,
    is_accepted,
    score,
    owner__user_id as owner_user_id,
    owner__account_id as owner_account_id,
    owner__display_name as owner_display_name,
    owner__reputation as owner_reputation,
    owner__user_type as owner_user_type,
    owner__accept_rate as owner_accept_rate,
    owner__profile_image as owner_profile_image,
    owner__link as owner_profile_link,
    content_license,
    TO_TIMESTAMP(creation_date ) as created_at,
    TO_TIMESTAMP(last_activity_date ) as last_activity_at,
    TO_TIMESTAMP(last_edit_date ) as last_edited_at,
    TO_TIMESTAMP(community_owned_date ) as community_owned_at,

    _dlt_load_id,
    _dlt_id
  from {{ source('raw_stackexchange', 'answers') }}
)
select * from source