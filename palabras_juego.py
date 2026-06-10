from database import get_db

db = get_db()

palabras =[
    ('drake', 'cantantes'),
    ('victormendivil', 'cantantes'),
    ('badbunny', 'cantantes'),
    ('neton', 'cantantes'),
    ('kendricklamar', 'cantantes'),
    ('feid', 'cantantes'),
    ('luismiguel', 'cantantes'),
    ('avengers', 'peliculas'),
    ('conjuro', 'peliculas'),
    ('fightclub', 'peliculas'),
    ('cars','peliculas'),
    ('spiderman', 'peliculas'),
    ('starwars', 'peliculas'),
    ('toystory', 'peliculas'),
    ('perro','animales'),
    ('gato','animales'),
    ('tigre','animales'),
    ('hipopotamo', 'animales'),
    ('elefante', 'animales'),
    ('simio', 'animales'),
    ('serpiente', 'animales'),
    ('minecraft', 'videojuegos'),
    ('fortnite', 'videojuegos'),
    ('pokemon', 'videojuegos'),
    ('zelda', 'videojuegos'),
    ('mario', 'videojuegos'),
    ('halo', 'videojuegos'),
    ('fifa', 'videojuegos'),
    ('callofduty', 'videojuegos'),
    ('gta', 'videojuegos'),
    ('mexico', 'paises'),
    ('brasil', 'paises'),
    ('argentina', 'paises'),
    ('japon', 'paises'),
    ('francia', 'paises'),
    ('alemania', 'paises'),
    ('australia', 'paises'),
    ('canada', 'paises'),
    ('egipto', 'paises'),
    ('china', 'paises'),
    ('pizza', 'comida'),
    ('hamburguesa', 'comida'),
    ('sushi', 'comida'),
    ('tacos', 'comida'),
    ('ramen', 'comida'),
    ('lasagna', 'comida'),
    ('burrito', 'comida'),
    ('enchiladas', 'comida'),
    ('ceviche', 'comida'),
    ('pozole', 'comida'),

]



db.executemany('INSERT INTO palabras (palabra, categoria) VALUES (?, ?)', palabras)
db.commit()
db.close()

print('Palabras agregadas')