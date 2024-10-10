import json
import os
from datetime import datetime
import uuid


class Task:
    """
    Represents a task with an ID, description, status, and timestamps.
    """

    def __init__(
        self, task_id, description, status="todo", createdAt=None, updatedAt=None
    ):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.createdAt = createdAt or datetime.now()
        self.updatedAt = updatedAt or self.createdAt

    def update_description(self, new_description):
        self.description = new_description
        self.updatedAt = datetime.now().isoformat()

    def update_status(self, new_status):
        self.status = new_status
        self.updatedAt = datetime.now().isoformat()

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat(),
        }


class TaskManager:
    def __init__(self, file_name="tasks.json"):
        self.file_name = file_name
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, "r") as file:
            try:
                task_dicts = json.load(file)
                return [
                    Task(
                        task_id=task["task_id"],
                        description=task["description"],
                        status=task["status"],
                        createdAt=datetime.fromisoformat(task["createdAt"]),
                        updatedAt=datetime.fromisoformat(task["updatedAt"]),
                    )
                    for task in task_dicts
                ]
            except json.JSONDecodeError:
                return []

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    def add_task(self, description: str) -> None:
        task_id = str(uuid.uuid4())
        new_task = Task(task_id, description)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task added successfully (ID: {task_id})")

    def update_task(self, task_id: int, new_description: str) -> None:
        for task in self.tasks:
            if task.task_id == task_id:
                task.update_description(new_description)
                self.save_tasks()
                print(f"Task updated successfully (ID: {task_id})")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id: int) -> None:
        initial_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        if len(self.tasks) < initial_length:
            self.save_tasks()
            print(f"Task deleted successfully (ID: {task_id})")
        else:
            print(f"Task with ID {task_id} not found.")

    def mark_task(self, task_id: int, status: str) -> None:
        for task in self.tasks:
            if task.task_id == task_id:
                task.update_status(status)
                self.save_tasks()
                print(f"Task marked as {status} (ID: {task_id})")
                return
        print(f"Task with ID {task_id} not found.")

    def list_tasks(self, status=None):
        tasks = (
            self.tasks
            if status is None
            else [task for task in self.tasks if task.status == status]
        )
        for task in sorted(tasks, key=lambda x: x.createdAt):
            color = self.get_status_color(task.status)
            reset_color = "\033[0m"
            print(
                f"{color}ID: {task.task_id}, Description: {task.description}, Status: {task.status}, "
                f"Created At: {task.createdAt}, Updated At: {task.updatedAt}{reset_color}"
            )

    def get_status_color(self, status: str) -> str:
        if status == "todo":
            return "\033[94m"  # Blue for 'todo'
        elif status == "in-progress":
            return "\033[93m"  # Yellow for 'in-progress'
        elif status == "done":
            return "\033[92m"  # Green for 'done'
        return "\033[0m"  # Default color
