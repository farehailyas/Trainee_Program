-- models/staging/stg_questions.sql
with source as (
  select
    question_id,
    title,
    is_answered,
    score,
    view_count,
    answer_count,
    TO_TIMESTAMP(creation_date ) as created_at,
    TO_TIMESTAMP(last_activity_date ) as last_activity_at,
    TO_TIMESTAMP(last_edit_date ) as last_edited_at,
    TO_TIMESTAMP(closed_date ) as closed_at,
    TO_TIMESTAMP(protected_date ) as protected_at,
    TO_TIMESTAMP(locked_date ) as locked_at,
    TO_TIMESTAMP(community_owned_date ) as community_owned_at,
    owner__user_id as owner_user_id,
    owner__account_id as owner_account_id,
    owner__display_name as owner_display_name,
    owner__reputation as owner_reputation,
    owner__user_type as owner_user_type,
    owner__accept_rate as owner_accept_rate,
    owner__profile_image as owner_profile_image,
    owner__link as owner_link,
    accepted_answer_id,
    closed_reason,
    link,
    content_license,
    _dlt_load_id,
    _dlt_id as question_dlt_id
  from {{ source('raw_stackexchange', 'questions') }}
)
select * from source