# Task Tracker CLI

A simple Command Line Interface (CLI) application to manage tasks. This project allows you to add, update, delete, and list tasks. It stores task data in a JSON file and provides functionalities to mark tasks as in-progress or done.

## Features

- Add a new task
- Update an existing task
- Delete a task
- Mark a task as in-progress or done
- List all tasks or filter by status

## Requirements

- Python 3.x

## Setup

**Clone the repository:**

```bash
git clone https://github.com/ZinF10/Task-Tracker-CLI.git
```

## Example

The list of commands and their usage is given below:

```bash
# Adding a new task
python main.py add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
python main.py update 1 "Buy groceries and cook dinner"
python main.py delete 1

# Marking a task as in progress or done
python main.py mark-in-progress 1
python main.py mark-done 1

# Listing all tasks
python main.py list

# Listing tasks by status
python main.py list done
python main.py list todo
python main.py list in-progress
```

## Project Page

You can find more details about this project and its roadmap here: [Task Tracker Project Roadmap](https://roadmap.sh/projects/task-tracker)