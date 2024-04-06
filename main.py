import threading
import time
from todolist import ToDoList
from task import Task

def reminder_scheduler(todo_list):
    """Function to check for task reminders periodically."""
    while True:
        todo_list.check_and_remind()
        time.sleep(86400)  # Check once every 24 hours, can adjust as needed

def main():
    todo_list = ToDoList()
    reminder_thread = threading.Thread(target=reminder_scheduler, args=(todo_list,), daemon=True)
    reminder_thread.start()

    commands = {
        'add': "Add a new task.",
        'remove': "Remove a task.",
        'update': "Update a task.",
        'list': "List all tasks.",
        'save': "Save tasks to file.",
        'load': "Load tasks from file.",
        'exit': "Exit the application."
    }

    while True:
        print("\nCommands:")
        for cmd, desc in commands.items():
            print(f"{cmd} - {desc}")
        cmd = input("Enter command: ").strip().lower()

        if cmd == 'add':
            description = input("Task description: ")
            due_date = input("Due date (YYYY-MM-DD, optional): ")
            deadline = input("Deadline (YYYY-MM-DD HH:MM, optional): ")
            task = Task(description, due_date if due_date else None, deadline if deadline else None)
            todo_list.add_task(task)
            print("Task added.")

        elif cmd == 'remove':
            index = int(input("Task index to remove: ")) - 1
            todo_list.remove_task(index)
            print("Task removed.")

        elif cmd == 'update':
            index = int(input("Task index to update: ")) - 1
            new_description = input("New description (optional): ")
            new_due_date = input("New due date (YYYY-MM-DD, optional): ")
            # Deadline updates can also be handled here if needed
            todo_list.update_task(index, new_description if new_description else None, new_due_date if new_due_date else None)
            print("Task updated.")

        elif cmd == 'list':
            todo_list.list_tasks()

        elif cmd == 'save':
            filename = input("Filename to save tasks: ")
            todo_list.save_to_file(filename)
            print("Tasks saved.")

        elif cmd == 'load':
            filename = input("Filename to load tasks from: ")
            todo_list.load_from_file(filename)
            print("Tasks loaded.")

        elif cmd == 'exit':
            print("Exiting...")
            break

        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
