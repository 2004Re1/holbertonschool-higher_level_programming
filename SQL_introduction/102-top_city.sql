-- ASKNJDAKF
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
WHERE month = 'July' or month = 'August'
ORDER BY AVG(value)
