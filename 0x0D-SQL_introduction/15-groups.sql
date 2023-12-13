-- Lists the number of record with the same score
SELECT age COUNT(*) AS number
FROM second_table
GROUP BY score
GROUP BY number DESC;
