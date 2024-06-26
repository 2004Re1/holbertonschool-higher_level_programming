-- jsaipfjaf
SELECT cities.id, cities.name, state.name FROM cities
INNER JOIN state ON state.id = cities.state_id
ORDER BY cities.id ASC;
