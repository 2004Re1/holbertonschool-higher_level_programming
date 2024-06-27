-- Assuming the database name is passed as an argument, for example 'hbtn_0d_tvshows'

SELECT name 
FROM tv_genres 
WHERE id NOT IN (
    SELECT genre_id 
    FROM tv_show_genres
    JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;

