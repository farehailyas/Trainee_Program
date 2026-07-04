WITH questions AS (
    SELECT question_id, title , view_count, answer_count
    FROM {{ ref('stg_questions') }}
),


comment_counts AS (
    SELECT post_id, COUNT(comment_id) AS comment_count
    FROM {{ ref('stg_comments') }}
    GROUP BY post_id
)

SELECT
    questions.question_id,questions.title,
    questions.view_count,
    questions.answer_count,
    COALESCE(comment_counts.comment_count, 0) AS comment_count
FROM questions
LEFT JOIN comment_counts
ON questions.question_id = comment_counts.post_id