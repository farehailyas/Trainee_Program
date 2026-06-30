SELECT p.id, i.transcript,p.address_street_name, MAX(p.address_number) as last_house
FROM person p 
JOIN interview i ON i.person_id = p.id
WHERE p.address_street_name = "Northwestern Dr"
GROUP BY p.id, i.transcript , p.address_street_name
HAVING p.address_number = MAX(p.address_number)
ORDER BY MAX(p.address_number) DESC
LIMIT 1
