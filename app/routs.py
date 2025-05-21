from flask import (
    Flask, 
    render_template
)
import requests as pyrequests

BACKEND_URL = "http://127.0.0.1:5000/tasks"

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/tasks")
def list_tasks():
    response = pyrequests.get(BACKEND_URL)
    if response.status_code == 200:
        tasks_list = response.json()["tasks"]
        return render_template("list.html", tasks=tasks_list)
    return (
        render_template("error.html", error=response.status_code),
        response.status_code
    )