-- List all records of a table
-- Display <score> and <name> in descending order according to score

-- SHOW FIELDS FROM second_table;
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
