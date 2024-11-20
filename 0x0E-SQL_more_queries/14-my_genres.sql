-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tg.name
FROM tv_genres
JOIN tv_show_genres ts ON tg.id = ts.genre_id
JOIN tv_shows ON tv_shows.id = ts.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY tg.name
