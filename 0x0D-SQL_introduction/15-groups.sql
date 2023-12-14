-- Lists the number of record with the same score
SELECT score, COUNT(name) AS "number"
FROM second_table
GROUP BY score
GROUP BY number DESC;
