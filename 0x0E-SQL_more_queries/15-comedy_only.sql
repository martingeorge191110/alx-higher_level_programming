-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT ts.title
FROM tv_shows ts, tv_show_genres tsg, tv_genres tg
WHERE ts.id = tsg.show_id 
   AND tg.id = tsg.genre_id 
   AND tg.name = "Comedy"
ORDER BY ts.title;
