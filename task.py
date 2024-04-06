from datetime import datetime, timedelta

class Task:
    def __init__(self, description, due_date=None, deadline=None, completed=False):
        self.description = description
        self.completed = completed  # Accept completed status
        self.due_date = due_date
        self.deadline = deadline

    def mark_as_completed(self):
        self.completed = True

    def update_description(self, new_description):
        self.description = new_description

    def update_due_date(self, new_due_date):
        self.due_date = new_due_date

    def is_deadline_approaching(self):
        if not self.deadline:
            return False
        deadline_datetime = datetime.strptime(self.deadline, '%Y-%m-%d %H:%M')
        return deadline_datetime - datetime.now() < timedelta(days=1)  # Reminder 1 day before
