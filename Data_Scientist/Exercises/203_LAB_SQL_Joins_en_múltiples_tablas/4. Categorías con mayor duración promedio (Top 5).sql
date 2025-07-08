SELECT 
    c.name AS category,
    ROUND(AVG(f.length), 2) AS avg_duration
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
GROUP BY c.name
ORDER BY avg_duration DESC
LIMIT 5;