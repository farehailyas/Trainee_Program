SELECT p.id, p.name , d.hair_color ,d.car_make , d.car_model,f.event_name , COUNT(f.event_name) as attend_count
FROM person p
JOIN drivers_license d 
ON d.id = p.license_id
JOIN facebook_event_checkin f 
ON p.id = f.person_id
WHERE d.hair_color = 'red' AND gender = 'female' AND d.height BETWEEN 65 AND 67 
AND f.event_name = "SQL Symphony Concert" AND f.date LIKE "201712%"
GROUP BY p.id, p.name
HAVING COUNT(f.event_name) = 3;
