//second witness
SELECT * 
FROM person p 
JOIN interview i
ON i.person_id = p.id
where p.name Like "%Annabel%" AND p.address_street_name = "Franklin Ave"
