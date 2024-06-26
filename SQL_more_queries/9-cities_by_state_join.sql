-- jsaipfjaf
SELECT cities.id AS id, cities.name AS name, state.name AS name FROM cities
INNER JOIN state ON state.id = cities.state_id
ORDER BY cities.id ASC;
