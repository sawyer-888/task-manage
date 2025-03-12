from fastapi import FastAPI, HTTPException
from database import init_db, get_db_connection
from models import Task
import sqlite3

app = FastAPI()

# Initialize the database
init_db()

@app.post("/tasks/")
def create_task(task: Task):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title, description, priority, deadline, completed) VALUES (?, ?, ?, ?, 0)",
                   (task.title, task.description, task.priority, task.deadline))
    conn.commit()
    conn.close()
    return {"message": "Task created successfully"}

@app.get("/tasks/")
def get_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return [{"id": t[0], "title": t[1], "description": t[2], "priority": t[3], "deadline": t[4], "completed": t[5]} for t in tasks]

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title=?, description=?, priority=?, deadline=? WHERE id=?",
                   (task.title, task.description, task.priority, task.deadline, task_id))
    conn.commit()
    conn.close()
    return {"message": "Task updated successfully"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return {"message": "Task deleted successfully"}
