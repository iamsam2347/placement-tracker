from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# 🔧 Create DB if not exists
def init_db():
    with sqlite3.connect("tasks.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                task TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)
init_db()

# 🏠 Homepage: Dashboard
@app.route('/')
def dashboard():
    with sqlite3.connect("tasks.db") as conn:
        tasks = conn.execute("SELECT * FROM tasks").fetchall()
    return render_template("dashboard.html", tasks=tasks)

# ➕ Add Task Route
@app.route('/add', methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        date = request.form["date"]
        task = request.form["task"]
        status = request.form["status"]
        with sqlite3.connect("tasks.db") as conn:
            conn.execute("INSERT INTO tasks (date, task, status) VALUES (?, ?, ?)", (date, task, status))
        return redirect('/')
    return render_template("add_task.html")

# 🚀 Run App
if __name__ == "__main__":
    app.run(debug=True)
