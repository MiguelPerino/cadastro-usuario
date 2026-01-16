import sqlite3
import os

DB_NAME = 'database.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )            
    ''')

    conn.commit()
    conn.close()

def insert_user(nome, email, senha_hash):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)',
        (nome, email, senha_hash)
    )

    conn.commit()
    conn.close()


def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM users WHERE email = ?',
        (email,)
    )

    user = cursor.fetchone()
    conn.close()
    return user

