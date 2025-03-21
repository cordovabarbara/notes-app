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
#new_note("Mi primera nota", "Este es el contenido de mi primera nota.")

#Funcion para tener todas la notas
def get_notes():
    with conect_db() as conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM notes'
        cursor.execute(query)
        return cursor.fetchall()
    
#Funcion para tener todas la notas por id
def get_note_by_id(id):
    with conect_db() as conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM notes WHERE id = ?'
        cursor.execute(query, (id,))
        note = cursor.fetchone()
    if note is None:
        return f"No se encontro una nota con el ID {id}"
    return note

#print(get_note_by_id(100))

#Funcion para eliminar notar por id
def delete_note(id):
    with conect_db() as conn:
        cursor = conn.cursor()
        query = 'DELETE FROM notes WHERE id =?'
        cursor.execute(query, (id,))
        if cursor.rowcount == 0:
            return f"No existe una nota con el id{id}"
        conn.commit()
        return f"Nota con ID {id} eliminada exitosamente"