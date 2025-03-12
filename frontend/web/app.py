from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000/tasks/"

@app.route("/")
def index():
    tasks = requests.get(API_URL).json()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    title = request.form["title"]
    description = request.form["description"]
    priority = request.form["priority"]
    deadline = request.form["deadline"]

    requests.post(API_URL, json={
        "title": title,
        "description": description,
        "priority": int(priority),
        "deadline": deadline
    })
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    requests.delete(f"{API_URL}{task_id}")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
