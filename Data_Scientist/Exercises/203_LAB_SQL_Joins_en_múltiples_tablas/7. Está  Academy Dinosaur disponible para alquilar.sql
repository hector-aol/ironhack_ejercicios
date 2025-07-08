SELECT 
    f.title,
    COUNT(i.inventory_id) AS available_copies
FROM film f
LEFT JOIN inventory i 
    ON f.film_id = i.film_id
    AND NOT EXISTS (
        SELECT 1
        FROM rental r
        WHERE r.inventory_id = i.inventory_id
        AND r.return_date IS NULL
    )
WHERE f.title = 'ACADEMY DINOSAUR'
GROUP BY f.title;