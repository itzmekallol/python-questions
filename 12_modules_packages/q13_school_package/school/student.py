"""
student.py — part of the school package.
"""


class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name} (Roll {self.roll_number}) - Marks: {self.marks}"
