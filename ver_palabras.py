from database import get_db

db = get_db()
palabras = db.execute("SELECT * FROM palabras").fetchall()

for p in palabras:
    print(p['palabra'], '-', p['categoria'])

print(f'\nTotal: {len(palabras)} palabras')
db.close()