-- List all citites in database and their state id, use join
SELECT cities.id, cities.name, states.name
FROM cities 
CROSS JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
