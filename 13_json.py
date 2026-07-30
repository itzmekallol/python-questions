"""
Python Practice — JSON (15 Questions)
Solutions with explanations.

Run this file with: python python_json_practice.py

Rules followed throughout:
- Uses Python's built-in json module exclusively.
- Uses `with open(...)` for all file operations.
- Data is built as dictionaries/lists first, then converted to JSON.
- File-related errors (missing file, bad JSON) are handled explicitly.

All JSON files this script creates live in a "practice_files" folder
next to this script, so nothing clutters your main working directory.
Wherever input() would normally be used, sample fallback values are used
instead so the script runs end-to-end without manual entry.
"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# =========================================================
# PART 1: JSON BASICS (1-5)
# =========================================================

print("=" * 50)
print("PART 1: JSON BASICS")
print("=" * 50)

# --- Q1: Dictionary -> JSON string ---
student_dict = {"name": "Kallol", "age": 20, "course": "Python"}
student_json_string = json.dumps(student_dict)
print("\nQ1: JSON string:")
print(student_json_string)

# --- Q2: JSON string -> Python dictionary ---
student_json_input = '{"name": "Isha", "age": 21, "course": "Data Science"}'
parsed_student = json.loads(student_json_input)
print("\nQ2: Parsed dictionary values:")
for key, value in parsed_student.items():
    print(f"{key}: {value}")

# --- Q3: List of five numbers -> JSON string ---
numbers_list = [10, 25, 33, 47, 52]
numbers_json_string = json.dumps(numbers_list)
print("\nQ3: JSON string:", numbers_json_string)

# --- Q4: Nested dictionary -> formatted (indented) JSON string ---
nested_student = {
    "personal_details": {"name": "Aarav", "age": 20},
    "marks": {"math": 88, "science": 92, "english": 79},
    "address": {"city": "Kolkata", "state": "West Bengal", "pincode": "700001"},
}
formatted_json_string = json.dumps(nested_student, indent=4)
print("\nQ4: Formatted JSON string:")
print(formatted_json_string)

# --- Q5: User input (name, age, city) -> dictionary -> JSON ---
# name_input = input("Enter your name: ")
# age_input = int(input("Enter your age: "))
# city_input = input("Enter your city: ")
name_input, age_input, city_input = "Kallol", 20, "Kolkata"  # sample values
user_info = {"name": name_input, "age": age_input, "city": city_input}
user_info_json = json.dumps(user_info)
print("\nQ5: JSON string from user input:")
print(user_info_json)


# =========================================================
# PART 2: JSON FILES (6-10)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: JSON FILES")
print("=" * 50)

# --- Q6: Save a student dictionary to student.json ---
student_record = {"name": "Priya", "age": 22, "course": "Machine Learning", "marks": 91}

try:
    with open(path("student.json"), "w") as f:
        json.dump(student_record, f, indent=4)
    print("\nQ6: student.json saved successfully")
except IOError as e:
    print(f"\nQ6: Error writing file: {e}")

# --- Q7: Read student.json and display it nicely ---
def load_json_file(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: '{filename}' does not exist")
        return None
    except json.JSONDecodeError:
        print(f"Error: '{filename}' contains invalid JSON")
        return None

print("\nQ7: Contents of student.json (user-friendly):")
loaded_student = load_json_file(path("student.json"))
if loaded_student:
    for key, value in loaded_student.items():
        print(f"{key.title()}: {value}")

# --- Q8: List of student dictionaries -> students.json ---
students_data = [
    {"roll_no": "R01", "name": "Aarav", "marks": 88},
    {"roll_no": "R02", "name": "Isha", "marks": 92},
    {"roll_no": "R03", "name": "Vikram", "marks": 76},
]

try:
    with open(path("students.json"), "w") as f:
        json.dump(students_data, f, indent=4)
    print("\nQ8: students.json saved successfully")
except IOError as e:
    print(f"\nQ8: Error writing file: {e}")

# --- Q9: Load students.json and display every student ---
print("\nQ9: All students in students.json:")
loaded_students = load_json_file(path("students.json"))
if loaded_students:
    for student in loaded_students:
        print(f"{student['roll_no']} - {student['name']} - Marks: {student['marks']}")

# --- Q10: Append a new student to students.json without losing existing data ---
def append_student(filename, new_student):
    try:
        with open(filename, "r") as f:
            students = json.load(f)
    except FileNotFoundError:
        students = []
    except json.JSONDecodeError:
        print("Error: existing file contains invalid JSON; starting a new list")
        students = []

    students.append(new_student)

    try:
        with open(filename, "w") as f:
            json.dump(students, f, indent=4)
        return students
    except IOError as e:
        print(f"Error writing file: {e}")
        return students

print("\nQ10: After appending a new student:")
new_student_record = {"roll_no": "R04", "name": "Diana", "marks": 85}
updated_students = append_student(path("students.json"), new_student_record)
for student in updated_students:
    print(f"{student['roll_no']} - {student['name']} - Marks: {student['marks']}")


# =========================================================
# PART 3: JSON PROCESSING (11-13)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: JSON PROCESSING")
print("=" * 50)

# --- Q11: Search for a student by name ---
def search_student_by_name(filename, target_name):
    students = load_json_file(filename)
    if students is None:
        return None
    for student in students:
        if student["name"].lower() == target_name.lower():
            return student
    return None

print("\nQ11: Search for 'Isha':")
found_student = search_student_by_name(path("students.json"), "Isha")
print(found_student if found_student else "Student not found")

print("Search for 'Zara' (not present):")
found_student2 = search_student_by_name(path("students.json"), "Zara")
print(found_student2 if found_student2 else "Student not found")

# --- Q12: Update a student's marks and save changes ---
def update_student_marks(filename, target_name, new_marks):
    students = load_json_file(filename)
    if students is None:
        return False
    updated = False
    for student in students:
        if student["name"].lower() == target_name.lower():
            student["marks"] = new_marks
            updated = True
    if updated:
        try:
            with open(filename, "w") as f:
                json.dump(students, f, indent=4)
        except IOError as e:
            print(f"Error writing file: {e}")
            return False
    return updated

print("\nQ12: Updating Vikram's marks to 95:")
success = update_student_marks(path("students.json"), "Vikram", 95)
print("Update successful:", success)
print("Confirming update:", search_student_by_name(path("students.json"), "Vikram"))

# --- Q13: Delete a student by name, save updated data ---
def delete_student(filename, target_name):
    students = load_json_file(filename)
    if students is None:
        return False
    original_count = len(students)
    students = [s for s in students if s["name"].lower() != target_name.lower()]
    if len(students) == original_count:
        return False  # nothing was removed
    try:
        with open(filename, "w") as f:
            json.dump(students, f, indent=4)
        return True
    except IOError as e:
        print(f"Error writing file: {e}")
        return False

print("\nQ13: Deleting 'Aarav':")
delete_success = delete_student(path("students.json"), "Aarav")
print("Deletion successful:", delete_success)
print("Remaining students:")
for student in load_json_file(path("students.json")):
    print(f"{student['roll_no']} - {student['name']} - Marks: {student['marks']}")


# =========================================================
# PART 4: REAL-WORLD MINI PROJECTS (14-15)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: REAL-WORLD MINI PROJECTS")
print("=" * 50)

# --- Q14: Contact Book (JSON-backed) ---
class ContactBookJSON:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Warning: contact file contained invalid JSON; starting fresh")
            return {}

    def _save(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.contacts, f, indent=4)
        except IOError as e:
            print(f"Error saving contacts: {e}")

    def add_contact(self, name, phone, email):
        self.contacts[name] = {"phone": phone, "email": email}
        self._save()
        return f"Contact '{name}' added"

    def search_contact(self, name):
        return self.contacts.get(name, "Contact not found")

    def update_contact(self, name, phone=None, email=None):
        if name not in self.contacts:
            return "Contact not found"
        if phone:
            self.contacts[name]["phone"] = phone
        if email:
            self.contacts[name]["email"] = email
        self._save()
        return f"Contact '{name}' updated"

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            self._save()
            return f"Contact '{name}' deleted"
        return "Contact not found"

    def display_all(self):
        return self.contacts

print("\nQ14: Contact Book (JSON)")
contact_book = ContactBookJSON(path("contacts.json"))
print(contact_book.add_contact("Ravi", "9876543210", "ravi@example.com"))
print(contact_book.add_contact("Meena", "9123456780", "meena@example.com"))
print("Search 'Ravi':", contact_book.search_contact("Ravi"))
print(contact_book.update_contact("Ravi", phone="9999999999"))
print("All contacts:", contact_book.display_all())
print(contact_book.delete_contact("Meena"))
print("All contacts after deletion:", contact_book.display_all())

# --- Q15: Library Management System (JSON-backed) ---
class LibraryManagementJSON:
    def __init__(self, filename):
        self.filename = filename
        self.books = self._load()  # loads automatically when the program starts

    def _load(self):
        if not os.path.exists(self.filename):
            return {}
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Warning: library file contained invalid JSON; starting fresh")
            return {}

    def _save(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.books, f, indent=4)
        except IOError as e:
            print(f"Error saving library data: {e}")

    def add_book(self, book_id, title, author, copies=1):
        if book_id in self.books:
            return f"Book ID {book_id} already exists"
        self.books[book_id] = {
            "title": title,
            "author": author,
            "available_copies": copies,
        }
        self._save()
        return f"Book '{title}' added"

    def remove_book(self, book_id):
        if book_id in self.books:
            removed_title = self.books[book_id]["title"]
            del self.books[book_id]
            self._save()
            return f"Book '{removed_title}' removed"
        return "Book not found"

    def search_book(self, book_id):
        return self.books.get(book_id, "Book not found")

    def issue_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            return "Book not found"
        if book["available_copies"] <= 0:
            return f"No copies of '{book['title']}' available"
        book["available_copies"] -= 1
        self._save()
        return f"Issued '{book['title']}'. Remaining copies: {book['available_copies']}"

    def return_book(self, book_id):
        book = self.books.get(book_id)
        if not book:
            return "Book not found"
        book["available_copies"] += 1
        self._save()
        return f"Returned '{book['title']}'. Available copies: {book['available_copies']}"

    def display_all(self):
        return self.books

print("\nQ15: Library Management System (JSON)")
library_json = LibraryManagementJSON(path("library.json"))
print(library_json.add_book("B1", "The Hobbit", "J.R.R. Tolkien", 2))
print(library_json.add_book("B2", "1984", "George Orwell", 1))
print(library_json.issue_book("B2"))
print(library_json.issue_book("B2"))  # no copies left
print(library_json.return_book("B2"))
print("Search B1:", library_json.search_book("B1"))
print("All books:", library_json.display_all())
print(library_json.remove_book("B1"))
print("All books after removal:", library_json.display_all())

# Demonstrate that data was actually persisted and reloads correctly
print("\nReloading LibraryManagementJSON from disk to confirm persistence:")
library_reloaded = LibraryManagementJSON(path("library.json"))
print("Books after reload:", library_reloaded.display_all())

print("\n" + "=" * 50)
print(f"All JSON files are stored in: {DATA_DIR}")
print("=" * 50)