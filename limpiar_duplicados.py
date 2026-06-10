from database import get_db

db = get_db()

db.execute('''
    DELETE FROM palabras
    WHERE id NOT IN (
        SELECT MIN(id) FROM palabras GROUP BY palabra
    )
''')

db.commit()
db.close()
print('Duplicados eliminados')