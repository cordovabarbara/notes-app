import sqlite3

DATABASE_NAME = "notes.db"

def conect_db():
    return sqlite3.connect(DATABASE_NAME)

def create_table():
    with conect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )''')
        conn.commit()

def new_note(title, content):
    with conect_db() as conn:
        conn.execute('''
            INSERT INTO notes (title, content)
            VALUES (?, ?)
        ''', (title, content))
        conn.commit()

#crea la tabla si no existe
create_table()

#agregar nota
new_note("Mi primera nota", "Este es el contenido de mi primera nota.")