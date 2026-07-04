-- models/staging/stg_comments.sql
with source as (
  select
    comment_id,
    post_id,
    score,
    edited,
    TO_TIMESTAMP(creation_date) as created_at,
    owner__user_id as owner_user_id,
    owner__account_id as owner_account_id,
    owner__display_name as owner_display_name,
    owner__reputation as owner_reputation,
    owner__user_type as owner_user_type,
    owner__accept_rate as owner_accept_rate,
    owner__profile_image as owner_profile_image,
    owner__link as owner_link,
    reply_to_user__user_id as reply_to_user_id,
    reply_to_user__account_id as reply_to_user_account_id,
    reply_to_user__display_name as reply_to_user_display_name,
    reply_to_user__reputation as reply_to_user_reputation,
    reply_to_user__user_type as reply_to_user_user_type,
    reply_to_user__accept_rate as reply_to_user_accept_rate,
    reply_to_user__profile_image as reply_to_user_profile_image,
    reply_to_user__link as reply_to_user_link,
    content_license,
    _dlt_load_id,
    _dlt_id
  from {{ source('raw_stackexchange', 'comments') }}
)
select * from source