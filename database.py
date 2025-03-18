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
def new_note():
    with conect_db() as conn:
        conn.execute


create_table()