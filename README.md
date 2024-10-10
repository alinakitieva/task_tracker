# Task Tracker CLI

Task Tracker CLI is a command-line tool to manage your daily tasks. It allows you to add, update, delete, mark tasks with statuses (e.g., "in-progress", "done"), and filter tasks by their current status.

## Features

- **Add Tasks**: Create new tasks with a description.
- **Update Tasks**: Modify the description of an existing task.
- **Delete Tasks**: Remove tasks from the list.
- **Mark Tasks**: Change the status of a task to "in-progress" or "done".
- **List Tasks**: Display tasks, optionally filtered by their status (todo, in-progress, done).
- **Persistent Data**: All tasks are saved in a JSON file to maintain task records across sessions.

## Prerequisites

- Python 3 installed on your machine.

## Installation

**Clone the repository**:

   ```bash
   git clone https://github.com/alinakitieva/task_tracker.git
   cd task-tracker
   ```

## Usage

You can use the following commands to interact with the task tracker:

### 1. **Add a Task**

```bash
python main.py add "Your task description here"
```

Example:

```bash
python main.py add "Finish writing the project report"
```

Output:

```
Task added successfully (ID: 1)
```

### 2. **Update a Task**

```bash
python main.py update <task_id> "New task description"
```

Example:

```bash
python main.py update 1 "Complete the project report and email it"
```

Output:

```
Task updated successfully (ID: 1)
```

### 3. **Delete a Task**

```bash
python main.py delete <task_id>
```

Example:

```bash
python main.py delete 1
```

Output:

```
Task deleted successfully (ID: 1)
```

### 4. **Mark a Task as "in-progress" or "done"**

```bash
python main.py mark <task_id> <status>
```

Example:

```bash
python main.py mark 1 in-progress
```

Output:

```
Task marked as in-progress (ID: 1)
```

```bash
python main.py mark 1 done
```

Output:

```
Task marked as done (ID: 1)
```

### 5. **List All Tasks**

```bash
python main.py list
```

This will display all tasks regardless of their status.

Example:

```bash
python main.py list
```

Output:

```
ID: 1, Description: Complete the project report and email it, Status: done, Created At: 2024-10-10, Updated At: 2024-10-10
```

### 6. **List Tasks by Status**

You can filter tasks by their status:

```bash
python main.py list todo
python main.py list in-progress
python main.py list done
```

Example:

```bash
python main.py list todo
```

Output:

```
ID: 2, Description: Read the new research paper, Status: todo, Created At: 2024-10-10, Updated At: 2024-10-10
```

## File Structure

```text
task-tracker/
├── main.py        # Entry point for the CLI
├── tasks.py       # Contains the Task and TaskManager classes
├── tasks.json     # Stores tasks data persistently
└── README.md      # Documentation for the project
```

## Customization

- **Task Storage File**: By default, tasks are saved in `tasks.json` in the current directory. You can change this by modifying the `file_name` parameter in the `TaskManager` class.
- **Terminal Colors**: The CLI uses color codes to highlight task statuses (todo, in-progress, done). You can modify the color scheme by changing the `get_status_color` method in `tasks.py`.

## Future Improvements

- Add support for additional task attributes such as priority and due dates.
- Implement sorting options (e.g., by creation date or priority).
- Migrate task storage to a database (e.g., SQLite) for better performance and scalability.
- Add more comprehensive error handling and logging.
