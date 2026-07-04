WITH questions AS (
    SELECT
        question_id,
        created_at 
    FROM {{ ref('stg_questions') }}
),

answers AS (
    SELECT
        question_id,
        created_at 
    FROM {{ ref('stg_answers') }}
)

SELECT questions.question_id, questions.created_at,
DATEDIFF('minute',questions.created_at,  MIN(answers.created_at)) AS first_answer_time
FROM questions 
LEFT JOIN answers 
ON questions.question_id = answers.question_id
GROUP BY questions.question_id,questions.created_at
