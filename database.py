import sqlite3

def get_db():
    conn = sqlite3.connect('ahorcado.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS palabras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            categoria TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ranking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            puntaje INTEGER NOT NULL,
            fecha TEXT DEFAULT (date('now'))
        )
    ''')

    conn.commit()
    conn.close()
    print('Base de datos creada')

if __name__ == '__main__':
    init_db()