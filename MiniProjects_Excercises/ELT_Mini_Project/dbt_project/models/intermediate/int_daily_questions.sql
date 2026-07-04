WITH questions AS (
    SELECT question_id, created_at
    FROM {{ ref('stg_questions') }}
)

SELECT
DATE_TRUNC('day', created_at) as day,
COUNT(DISTINCT question_id) question_count
FROM questions
GROUP BY DATE_TRUNC('day', created_at) 
