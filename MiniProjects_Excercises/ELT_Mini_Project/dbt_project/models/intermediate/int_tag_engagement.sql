WITH question_engagement AS (
    SELECT
        question_id,
        view_count,
        answer_count,
        comment_count
    FROM {{ ref('int_question_engagement') }}
),

question_tags AS (
    SELECT
        question_id,
        tag_value
    FROM {{ ref('int_question_tag') }}
)

SELECT
    question_tags.tag_value,
    COUNT(question_engagement.question_id) AS question_count,
    ROUND(AVG(question_engagement.view_count), 2) AS avg_views_per_question,
    ROUND(AVG(question_engagement.answer_count), 2) AS avg_answers_per_question,
    ROUND(AVG(question_engagement.comment_count), 2) AS avg_comments_per_question
FROM question_tags
LEFT JOIN question_engagement
ON question_tags.question_id = question_engagement.question_id
GROUP BY question_tags.tag_value