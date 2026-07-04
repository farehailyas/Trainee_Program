WITH question_tag AS (
    SELECT tag_value , question_id
    FROM {{ref('int_question_tag')}}
),

question_answer_time AS(
    SELECT question_id , created_at , first_answer_time
    FROM {{ref('int_first_answer')}}
)

SELECT question_answer_time.question_id, question_tag.tag_value, 
        question_answer_time.created_at , question_answer_time.first_answer_time
FROM question_answer_time
LEFT JOIN question_tag
ON question_tag.question_id = question_answer_time.question_id
