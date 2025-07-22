from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        date = request.form["date"]
        task = request.form["task"]
        status = request.form["status"]
        with sqlite3.connect("tasks.db") as conn:
            conn.execute("INSERT INTO tasks (date, task, status) VALUES (?, ?, ?)", (date, task, status))
        return redirect("/")

    with sqlite3.connect("tasks.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        tasks = cur.fetchall()
    return render_template("dashboard.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=10000)

