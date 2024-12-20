-- script that displays the max temperature of each state (ordered by State name)
SELECT state, AVG(value) as max_temp FROM temperature
GROUP BY state
ORDER BY state DESC;
