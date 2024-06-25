-- jksadopfjapof
SELECT state, MAX(temp) AS max_temp FROM temperatures
GROUP BY state
ORDER BY state;
