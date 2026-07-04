WITH users AS (
  SELECT user_id,
    display_name,
    reputation,
    bronze_badge_count,
    gold_badge_count,
    silver_badge_count,
    accept_rate
  FROM {{ ref('stg_users') }}
)
SELECT
    user_id,
    display_name,
    reputation,
    bronze_badge_count + gold_badge_count + silver_badge_count AS badges_earned,
    accept_rate AS accepted_answer_rate
FROM users
