SELECT UPPER(state) AS state, COUNT(*) AS count
FROM assignments
GROUP BY state;