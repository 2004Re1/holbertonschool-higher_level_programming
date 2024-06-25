-- ASKNJDAKF
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
WHERE month IN (7,8)
ORDER BY AVG(value)
LIMIT 3;
