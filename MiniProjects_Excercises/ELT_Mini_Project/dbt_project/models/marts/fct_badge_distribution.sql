WITH badge_distribution_temp AS (
    SELECT *
    FROM {{ ref('int_badge_distribution') }}
),

badge_distribution AS(
    SELECT
    badge_class,
    total_awards,
    ROUND(total_awards * 100.0 / SUM(total_awards) OVER (),2) AS percentage_of_total_awards
    FROM badge_distribution_temp
)
SELECT *
FROM badge_distribution