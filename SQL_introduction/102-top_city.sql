-- Query to display the top 3 cities with the highest average temperatures during July and August
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8) -- Filter by July and August
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
