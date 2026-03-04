import sqlite3

DB_NAME = 'database.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_task_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            titulo TEXT NOT NULL
            descricao TEXT
            data_limite TEXT
            concluida INTEGER DEFAULT 0,
            criada_em TEXT DEFAULT (datetime('now', 'localtime')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_task(user_id, titulo, descricao, data_limite):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO tasks (user_id, titulo, descricao, data_limite) VALUES (?, ?, ?, ?)',
        (user_id, titulo, descricao, data_limite)
    )

    conn.commit()
    conn.close()

def get_tasks_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'SELECT * FROM tasks WHERE user_id = ? ORDER BY concluida ASC, data_limite ASC',
        (user_id)
    )

    tasks = cursor.fetchall() #Returns all datas in tuples inside a list
    conn.close()
    return tasks

def toggle_task(task_id, user_id): #change task to conclued or not conclued
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE tasks SET concluida = CASE WHEN concluida = 1 THEN 0 ELSE 1 END WHERE id = ? AND user_id = ?',
        (task_id, user_id)
    )
    conn.commit()
    conn.close()

def delete_task(task_id, user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'DELETE FROM tasks WHERE id = ? AND user_id = ?',
        (task_id, user_id)
    )
    conn.commit()
    conn.close()