from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Home Route → Show dashboard + handle add task form
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

# ✅ Run Flask with PORT logic (important for Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(debug=False, host="0.0.0.0", port=port)
