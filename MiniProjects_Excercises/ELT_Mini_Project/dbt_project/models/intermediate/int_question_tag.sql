WITH questions AS (
    SELECT question_id,question_dlt_id, title
    FROM {{ ref('stg_questions') }}
),

question_tags AS (
    SELECT tag_value, question_id
    FROM {{ ref('stg_questions_tags') }}
)

SELECT question_tags.tag_value , questions.question_id
FROM questions
LEFT JOIN question_tags 
ON questions.question_dlt_id = question_tags.question_id
