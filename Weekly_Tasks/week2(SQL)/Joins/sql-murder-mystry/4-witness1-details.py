SELECT * 
FROM person p 
Join get_fit_now_member g
ON g.person_id = p.id
JOIN get_fit_now_check_in g_check
ON g_check.membership_id = g.id
JOIN drivers_license d
ON d.id = p.license_id
WHERE d.plate_number LIKE "%H42W%"

