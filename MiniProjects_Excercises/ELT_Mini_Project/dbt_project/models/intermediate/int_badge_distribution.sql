WITH badges AS 
(
    SELECT
    rank AS badge_class,
    award_count
    FROM {{ ref('stg_badges') }}
)

SELECT
badge_class,
SUM(award_count) AS total_awards
FROM badges
GROUP BY badge_class