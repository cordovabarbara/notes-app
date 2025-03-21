import sqlite3

DATABASE_NAME = "notes.db"

def conect_db():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    with conect_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL
            )''')
        conn.commit()

#crea una nueva nota
def new_note(title: str, content: str):
    with conect_db() as conn:
        conn.execute('''
            INSERT INTO notes (title, content)
            VALUES (?, ?)
        ''', (title, content))
        conn.commit()

#crea la tabla si no existe
create_table()

#agregar nota
#new_note("Mi segunda nota", "Lista a seguir para programar en Python.")

#Funcion para obtener todas la notas
def get_notes():
    with conect_db() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes")
        notes = cursor.fetchall()

        if not notes:
            return{"message": "No hay notas disponibles"}
        
        return [dict(note) for note in notes]

#Funcion para obtener  nota por id
def get_note_by_id(id):
    with conect_db() as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        query = 'SELECT * FROM notes WHERE id = ?'
        cursor.execute(query, (id,))
        note = cursor.fetchone()

    if note is None:
        return {"message": f"No se encontró una nota con el ID {id}"}
    
    return dict(note)

#Funcion para eliminar notar por id
def delete_note(id):
    with conect_db() as conn:
        cursor = conn.cursor()
        query = 'DELETE FROM notes WHERE id =?'
        cursor.execute(query, (id,))

        if cursor.rowcount == 0:
            return f"No existe una nota con el id {id}"
        
        conn.commit()
        return f"La Nota con ID {id} eliminada exitosamente"

#Funcion para actualizar nota, ya sea titulo o contenido o ambos
def update_note(id, title=None, content=None):
    try:
        with conect_db() as conn:
            cursor = conn.cursor()

# Verificar si el ID existe antes de actualizar
        cursor.execute("SELECT id FROM notes WHERE id = ?", (id,))
        if cursor.fetchone() is None:
                return f"No existe una nota con el ID {id}"
        
        update_fields = []
        values = []

        if title:
            update_fields.append("title = ?")
            values.append(title)
        if content:
            update_fields.append("content = ?")
            values.append(content)
        
        if not update_fields:
            return "No se proporcionaron valores para actualizar."

        query = f'''
                UPDATE notes
                SET {", ".join(update_fields)}
                WHERE id = ?
                '''
        values.append(id)

        cursor.execute(query, values)
        conn.commit()
        return f"La Nota con ID {id} fue actualiza exitosamente" 

    except sqlite3.Error as e:
        return f"Error al actualizar la nota: {e}"

