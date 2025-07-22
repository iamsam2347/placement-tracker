# init_db.py

import sqlite3

conn = sqlite3.connect('tasks.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        task TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("✅ Database initialized.")
