"""
classroom.py — part of the school package.
"""


class Classroom:
    def __init__(self, room_name, teacher):
        self.room_name = room_name
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average_marks(self):
        if not self.students:
            return 0
        return sum(s.marks for s in self.students) / len(self.students)

    def __str__(self):
        return f"Classroom {self.room_name} - Teacher: {self.teacher.name}"
