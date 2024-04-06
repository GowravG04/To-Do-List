import json
from task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if index < len(self.tasks):
            del self.tasks[index]

    def update_task(self, index, description=None, due_date=None):
        if index < len(self.tasks):
            if description:
                self.tasks[index].update_description(description)
            if due_date:
                self.tasks[index].update_due_date(due_date)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "Completed" if task.completed else "Pending"
            print(f"{i+1}. {task.description} - {status} - Due: {task.due_date}")

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.tasks = [Task(**task) for task in json.load(f)]

    def check_and_remind(self):
        for task in self.tasks:
            if not task.completed and task.is_deadline_approaching():
                print(f"Reminder: The deadline for '{task.description}' is approaching.")
