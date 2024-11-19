-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT TOP(3) city, temperature
FROM city_temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY temperature DESC;
