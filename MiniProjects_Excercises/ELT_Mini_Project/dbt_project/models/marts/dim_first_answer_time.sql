WITH first_answer_per_tag AS (
    SELECT tag_value , created_at , first_answer_time
    FROM {{ref('int_tag_first_answer')}}
),

average_time_to_answer_per_tag AS(
    SELECT tag_value , DATE_TRUNC('month' , created_at) AS month,
    AVG(first_answer_time) avg_time_to_first_answer_minutes
    FROM first_answer_per_tag
    GROUP BY tag_value,DATE_TRUNC('month', created_at)
)
SELECT *
FROM average_time_to_answer_per_tag