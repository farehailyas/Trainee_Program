WITH users_contributions AS(
    SELECT user_id , display_name , reputation, 
    RANK() OVER(ORDER BY reputation DESC) as rank_by_reputation ,
    badges_earned , RANK() OVER( ORDER BY badges_earned DESC) as rank_by_total_badges ,
    accepted_answer_rate , RANK() OVER( ORDER BY accepted_answer_rate DESC NULLS LAST) as rank_by_accepted_answer_rate 

    FROM {{ (ref('int_users_badges_count')) }}
)
SELECT *
FROM users_contributions