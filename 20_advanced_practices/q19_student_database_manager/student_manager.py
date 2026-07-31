"""
student_manager.py — the StudentManager class used by main.py.

Q19: Student Database Manager (backed by a JSON file).

Kept in its own module so the OOP logic is separated from the
demonstration/entry-point code in main.py, per the "use modules" rule.
"""

import json
import os


class StudentManagerError(Exception):
    """Base exception for student manager errors."""
    pass


class DuplicateRollNumberError(StudentManagerError):
    pass


class StudentNotFoundError(StudentManagerError):
    pass


class StudentManager:
    def __init__(self, filename):
        self.filename = filename
        self.students = self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: '{self.filename}' contained invalid JSON; starting fresh")
            return {}

    def _save(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.students, f, indent=4)
        except IOError as e:
            print(f"Error saving student data: {e}")

    def add_student(self, roll_no, name, marks):
        if roll_no in self.students:
            raise DuplicateRollNumberError(f"Roll number '{roll_no}' already exists")
        self.students[roll_no] = {"name": name, "marks": marks}
        self._save()
        return f"Student '{name}' added"

    def update_student(self, roll_no, name=None, marks=None):
        if roll_no not in self.students:
            raise StudentNotFoundError(f"No student found with roll number '{roll_no}'")
        if name is not None:
            self.students[roll_no]["name"] = name
        if marks is not None:
            self.students[roll_no]["marks"] = marks
        self._save()
        return f"Student '{roll_no}' updated"

    def delete_student(self, roll_no):
        if roll_no not in self.students:
            raise StudentNotFoundError(f"No student found with roll number '{roll_no}'")
        removed_name = self.students[roll_no]["name"]
        del self.students[roll_no]
        self._save()
        return f"Student '{removed_name}' deleted"

    def search_student(self, roll_no):
        if roll_no not in self.students:
            raise StudentNotFoundError(f"No student found with roll number '{roll_no}'")
        return self.students[roll_no]

    def sort_by_marks(self, descending=True):
        return sorted(
            self.students.items(),
            key=lambda item: item[1]["marks"],
            reverse=descending,
        )

    def export_summary(self):
        if not self.students:
            return "No students on record."
        marks_list = [s["marks"] for s in self.students.values()]
        return (
            f"Total students: {len(self.students)}\n"
            f"Average marks: {sum(marks_list) / len(marks_list):.2f}\n"
            f"Highest marks: {max(marks_list)}\n"
            f"Lowest marks: {min(marks_list)}"
        )
