import json, os.path as op

from models import Task

base_dir = op.abspath(op.dirname(__file__))
file_name = "tasks.json"


def load_data(file_name=file_name):
    with open(op.join(base_dir, "data", file_name), encoding="utf-8") as f:
        return json.load(f)
   
    
def save_data(tasks, file_name=file_name):
    with open(op.join(base_dir, "data", file_name), 'w') as f:
        json.dump(tasks, f, indent=4)


def add_task(description):
    tasks = load_data()
    task_id = len(tasks) + 1
    task = Task(id=task_id, description=description)
    tasks.append(task.to_dict())
    save_data(tasks)
    print(f'Task added successfully (ID: {task_id})')
    
    
def list_tasks(status=None):
    tasks = load_data()
    filtered_tasks = []
    for task_data in tasks:
        task = Task.from_dict(task_data)
        if not status or task.status == status:
            filtered_tasks.append(task)

    for task in filtered_tasks:
        print(f"ID: {task.id} | Desc: {task.description} | Status: {task.status}")
        
    
def update_task(task_id, new_description):
    tasks = load_data()
    for i, task_data in enumerate(tasks):
        if task_data['id'] == task_id:
            task = Task.from_dict(task_data)
            task.update_description(new_description)
            tasks[i] = task.to_dict()
            save_data(tasks)
            print(f'Task updated successfully !!!')
            return
    print('Task not found !!!')


def mark_task(task_id, status):
    tasks = load_data()
    for i, task_data in enumerate(tasks):
        if task_data['id'] == task_id:
            task = Task.from_dict(task_data)
            task.update_status(status)
            tasks[i] = task.to_dict()
            save_data(tasks)
            print(f'Task marked as {status}')
            return
    print('Task not found !!!')
    
    
def delete_task(task_id):
    tasks = load_data()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_data(tasks)
    print(f'Task with ID {task_id} deleted successfully')