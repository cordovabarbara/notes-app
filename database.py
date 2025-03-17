import sqlite3

def conecta_db():
    return sqlite3.connect('notes.db')