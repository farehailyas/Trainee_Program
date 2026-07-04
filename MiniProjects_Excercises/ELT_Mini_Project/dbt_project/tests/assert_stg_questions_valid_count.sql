-- tests/stg_questions_valid_counts.sql
SELECT *
FROM {{ ref('stg_questions') }}
WHERE view_count < 0
  OR answer_count < 0
  OR score IS NULL