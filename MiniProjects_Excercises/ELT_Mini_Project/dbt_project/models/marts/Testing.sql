
WITH abc AS (
    SELECT
    question_id,
    created_at,
    first_answer_time
FROM {{ ref('int_first_answer') }}
ORDER BY first_answer_time DESC
LIMIT 10
)
SELECT * FROM abc