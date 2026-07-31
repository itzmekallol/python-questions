"""
Q13: Task Management System.

Classes: User, Task, Project.
Features: add task, assign task, update status, set deadlines, display
pending tasks.

Run with: python main.py
"""

from datetime import date


class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Task:
    VALID_STATUSES = ("Pending", "In Progress", "Completed")

    _next_task_id = 1

    def __init__(self, title, deadline=None):
        self.task_id = Task._next_task_id
        Task._next_task_id += 1
        self.title = title
        self.assigned_to = None
        self.status = "Pending"
        self.deadline = deadline

    def assign(self, user):
        self.assigned_to = user

    def update_status(self, new_status):
        if new_status not in Task.VALID_STATUSES:
            raise ValueError(f"Invalid status '{new_status}'. Must be one of {Task.VALID_STATUSES}")
        self.status = new_status

    def __str__(self):
        assignee = self.assigned_to.name if self.assigned_to else "Unassigned"
        deadline_str = self.deadline.strftime("%d-%m-%Y") if self.deadline else "No deadline"
        return f"Task[{self.task_id}] '{self.title}' - {self.status} - {assignee} - Due {deadline_str}"


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, title, deadline=None):
        task = Task(title, deadline)
        self.tasks.append(task)
        return task

    def pending_tasks(self):
        return [task for task in self.tasks if task.status != "Completed"]


def main():
    print("Q13: Task Management System")

    project = Project("Website Redesign")
    alice = User("U1", "Alice")
    bob = User("U2", "Bob")

    task1 = project.add_task("Design homepage mockup", deadline=date(2026, 8, 5))
    task2 = project.add_task("Set up CI/CD pipeline", deadline=date(2026, 8, 10))
    task3 = project.add_task("Write API documentation", deadline=date(2026, 8, 8))

    task1.assign(alice)
    task2.assign(bob)
    task3.assign(alice)

    task1.update_status("In Progress")
    task2.update_status("Completed")

    print("\nAll tasks:")
    for task in project.tasks:
        print(task)

    print("\nPending tasks (not yet completed):")
    for task in project.pending_tasks():
        print(task)


if __name__ == "__main__":
    main()
