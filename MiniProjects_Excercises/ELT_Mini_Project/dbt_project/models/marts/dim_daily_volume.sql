WITH daily_questions AS (
    SELECT *
    FROM {{ref('int_daily_questions')}}
),
daily_answers AS (
    SELECT *
    FROM {{ref('int_daily_answers')}}
),
daily_comments AS (
    SELECT *
    FROM {{ref('int_daily_comments')}}
),

daily_volume AS (
    SELECT
    day,
    'Question' AS activity_type,
    question_count AS daily_volume
    FROM daily_questions

UNION ALL

    SELECT
    day,
    'Answer',
    answer_count
    FROM daily_answers

UNION ALL

    SELECT
    day,
    'Comment',
    comment_count
    FROM daily_comments
)
SELECT *
FROM daily_volume