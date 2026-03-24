# Student Task Manager

A full-stack task management web application built with Flask that allows users to create, organize, and manage tasks with priority levels.

## Live Demo
https://student-task-manager-gtos.onrender.com

## Features

- Add tasks with priority levels (Low, Medium, High)
- Color-coded priority badges
- Mark tasks as completed
- Undo completed tasks
- Delete tasks
- Persistent storage using JSON
- Clean and responsive user interface
- Empty state for better user experience

## Tech Stack

- Python
- Flask
- HTML
- CSS
- Jinja2
- JSON

## How It Works

Users can create tasks, assign a priority level, and manage them through a simple interface.  
Tasks are rendered dynamically using Jinja templates and stored in a JSON file so they remain available across sessions.

## Key Implementation Details

- Backend built with Flask routing and form handling
- Dynamic rendering with Jinja templates
- Local persistent storage using JSON
- Task completion toggle with updated UI state
- Deployed as a live web application on Render

## Run Locally

```bash
pip3 install -r requirements.txt
python3 app.py
