"""
main.py — imports classes from the school package and uses them together.

Q13: Demonstrates basic classes spread across package modules.

Run with: python main.py
"""

from school.student import Student
from school.teacher import Teacher
from school.classroom import Classroom

print("Q13: Using the school package")

teacher1 = Teacher("Mr. Verma", "Mathematics")
classroom1 = Classroom("10-A", teacher1)

classroom1.add_student(Student("Aarav", "R01", 85))
classroom1.add_student(Student("Isha", "R02", 92))
classroom1.add_student(Student("Vikram", "R03", 78))

print(classroom1)
for student in classroom1.students:
    print(student)
print("Average marks in classroom:", round(classroom1.average_marks(), 2))
