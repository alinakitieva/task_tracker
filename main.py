import argparse
from tasks import TaskManager


if __name__ == "__main__":
    task_manager = TaskManager()

    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("description", type=str, help="Description of the task")

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("task_id", type=int, help="ID of the task to update")
    update_parser.add_argument(
        "description", type=str, help="New description of the task"
    )

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")

    mark_parser = subparsers.add_parser("mark")
    mark_parser.add_argument("task_id", type=int, help="ID of the task to mark")
    mark_parser.add_argument(
        "status",
        type=str,
        choices=["in-progress", "done"],
        help="New status of the task",
    )

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument(
        "status",
        type=str,
        nargs="?",
        choices=["todo", "in-progress", "done"],
        help="Filter tasks by status",
    )

    args = parser.parse_args()

    if args.command == "add":
        task_manager.add_task(args.description)
    elif args.command == "update":
        task_manager.update_task(args.task_id, args.description)
    elif args.command == "delete":
        task_manager.delete_task(args.task_id)
    elif args.command == "mark":
        task_manager.mark_task(args.task_id, args.status)
    elif args.command == "list":
        task_manager.list_tasks(args.status)
