WITH answers AS (
  SELECT answer_id, created_at 
  FROM {{ ref('stg_answers') }}
)

SELECT
DATE_TRUNC('day', created_at) as day,
COUNT(DISTINCT answer_id) answer_count
FROM answers
GROUP BY DATE_TRUNC('day', created_at)
