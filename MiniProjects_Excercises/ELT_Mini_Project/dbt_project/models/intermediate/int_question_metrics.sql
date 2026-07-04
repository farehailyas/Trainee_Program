WITH questions AS (
    SELECT question_id, is_answered, title, view_count, answer_count
    FROM {{ ref('stg_questions') }}
)
SELECT question_id, title, is_answered, view_count, answer_count,  ROUND(answer_count / NULLIF(view_count,0) , 2) as  answer_to_view_ratio
FROM questions
