import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()

# Drop old table if needed (optional)
# cur.execute("DROP TABLE IF EXISTS tasks")

cur.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    task TEXT,
    start_date TEXT,
    end_date TEXT,
    difficulty_level TEXT,
    status TEXT
)
''')

conn.commit()
conn.close()
