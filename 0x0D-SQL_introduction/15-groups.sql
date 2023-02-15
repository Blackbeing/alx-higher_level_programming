-- List number of records with same value as group
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC
