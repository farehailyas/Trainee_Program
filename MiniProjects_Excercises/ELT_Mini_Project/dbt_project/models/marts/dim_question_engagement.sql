WITH tag_engagement AS (
    SELECT
        tag_value,
        question_count,
        avg_views_per_question,
        avg_answers_per_question,
        avg_comments_per_question
    FROM {{ ref('int_tag_engagement') }}
),

question_engagement AS(
    SELECT
    tag_value,
    question_count,
    avg_views_per_question,
    RANK() OVER (ORDER BY avg_views_per_question DESC) AS views_rank,
    avg_answers_per_question,
    RANK() OVER (ORDER BY avg_answers_per_question DESC) AS answers_rank,
    avg_comments_per_question,
    RANK() OVER (ORDER BY avg_comments_per_question DESC) AS comments_rank
    FROM tag_engagement
)

SELECT *
FROM question_engagement