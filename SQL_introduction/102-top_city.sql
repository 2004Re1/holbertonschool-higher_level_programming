-- ASKNJDAKF
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
WHERE month = 'July' OR month = 'August'
ORDER BY AVG(value);
