from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Database setup function
def init_db():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
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

# Run DB setup on app start
init_db()

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    if request.method == 'POST':
        date = request.form['date']
        task = request.form['task']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        difficulty = request.form['difficulty_level']
        status = request.form['status']

        cur.execute('''
            INSERT INTO tasks (date, task, start_date, end_date, difficulty_level, status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, task, start_date, end_date, difficulty, status))
        conn.commit()

    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    conn.close()
    return render_template('dashboard.html', tasks=tasks)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(debug=False, host='0.0.0.0', port=port)
