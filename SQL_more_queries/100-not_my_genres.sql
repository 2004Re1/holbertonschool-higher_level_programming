-- List all genres of the show Dexter from hbtn_0d_tvshows
SELECT tv_genres.name FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title IS NOT 'Dexter' 
ORDER BY tv_genres.name ASC;