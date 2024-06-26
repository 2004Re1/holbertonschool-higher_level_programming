-- Assuming the database name is passed as an argument, for example 'hbtn_0d_usa'

USE hbtn_0d_usa;

SELECT cities.id, cities.name, states.name AS state_name
FROM cities
INNER JOIN states ON states.id = cities.state_id
ORDER BY cities.id ASC;
