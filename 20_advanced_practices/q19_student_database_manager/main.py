"""
main.py — demonstrates the StudentManager (Q19: Student Database Manager).

Run with: python main.py
"""

import os
from student_manager import StudentManager, DuplicateRollNumberError, StudentNotFoundError

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


def main():
    print("Q19: Student Database Manager")
    manager = StudentManager(path("students.json"))

    print(manager.add_student("R01", "Aarav", 85))
    print(manager.add_student("R02", "Isha", 92))
    print(manager.add_student("R03", "Vikram", 76))

    try:
        manager.add_student("R01", "Duplicate Attempt", 50)
    except DuplicateRollNumberError as e:
        print("Caught error:", e)

    print(manager.update_student("R03", marks=88))

    try:
        manager.search_student("R99")
    except StudentNotFoundError as e:
        print("Caught error:", e)

    print("\nStudents sorted by marks (descending):")
    for roll_no, details in manager.sort_by_marks():
        print(f"{roll_no}: {details['name']} - {details['marks']}")

    print(manager.delete_student("R02"))

    print("\nSummary report:")
    print(manager.export_summary())


if __name__ == "__main__":
    main()
