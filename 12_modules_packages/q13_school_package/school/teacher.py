"""
teacher.py — part of the school package.
"""


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"Teacher: {self.name} (Subject: {self.subject})"
