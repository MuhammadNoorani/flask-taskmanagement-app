from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static')

# Route for your index.html file

tasks = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_tasks', methods=['POST'])
def add_tasks():
    global tasks
    tasks_list = request.json.get('tasks_list', None)
    if tasks_list:
        tasks.extend(tasks_list)
        message = f"Added {len(tasks_list)} tasks"
    else:
        message = "No tasks added"
    return jsonify({'message': message})


@app.route('/list_tasks', methods=['GET'])
def list_tasks():
    return jsonify({'tasks': tasks})


@app.route('/remove_task', methods=['POST'])
def remove_task():
    global tasks
    task_number = request.json.get('task_number', None)
    if task_number is not None and task_number.isdigit():
        task_number = int(task_number)
        if 1 <= task_number <= len(tasks):
            task = tasks.pop(task_number - 1)
            message = f"Removed task: {task}"
        else:
            message = "Invalid task number"
    else:
        message = "Invalid task number"

    return jsonify({'message': message})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
