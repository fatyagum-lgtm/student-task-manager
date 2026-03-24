from flask import Flask, request, redirect, render_template
import json
import os

app = Flask(__name__)

FILE = "tasks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

tasks = load_tasks()

@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_text = request.form.get('task')
    priority = request.form.get('priority')

    if task_text:
        tasks.append({
            "text": task_text,
            "priority": priority,
            "completed": False
        })
        save_tasks(tasks)

    return redirect('/')

@app.route('/delete/<int:index>')
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
    return redirect('/')

@app.route('/toggle/<int:index>')
def toggle_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = not tasks[index].get("completed", False)
        save_tasks(tasks)
    return redirect('/')

if __name__ == '__main__':
    app.run()
