
WITH comments AS (
    SELECT comment_id , created_at
    FROM {{ref('stg_comments')}}
)
 
SELECT
DATE_TRUNC('day', created_at) as day,
COUNT(DISTINCT comment_id) comment_count
FROM comments
GROUP BY DATE_TRUNC('day', created_at)

