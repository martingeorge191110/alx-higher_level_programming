--  lists all shows contained in the database hbtn_0d_tvshows
SELECT ts.title, tg.genre_id
FROM tv_shows t
LEFT JOIN tv_show_genres tg
ON ts.id = tg.show_id
ORDER BY ts.title, tg.genre_id
