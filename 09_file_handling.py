"""
Python Practice — File Handling (30 Questions)
Solutions with explanations.

Run this file with: python python_file_handling_practice.py

This script creates and manipulates real files so every example actually
works when you run it. All files it creates/reads live inside a folder
called "practice_files" next to this script, so nothing clutters your
main working directory. Wherever input() would normally be used, sample
fallback values are used instead so the script runs end-to-end without
manual entry — swap in input() calls when experimenting interactively.
"""

import os

# All demo files live in this folder so the script is self-contained
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    """Helper to build a full path inside the practice_files folder."""
    return os.path.join(DATA_DIR, filename)


# =========================================================
# PART 1: READING & WRITING FILES (1-8)
# =========================================================

print("=" * 50)
print("PART 1: READING & WRITING FILES")
print("=" * 50)

# --- Q1: Create hello.txt, write a message, then read it back ---
with open(path("hello.txt"), "w") as f:
    f.write("Welcome to Python File Handling!")

with open(path("hello.txt"), "r") as f:
    content = f.read()

print("\nQ1: Contents of hello.txt:")
print(content)

# --- Q2: Save user's name to name.txt, then read it back ---
# user_name = input("Enter your name: ")
user_name = "Kallol"  # sample value
with open(path("name.txt"), "w") as f:
    f.write(user_name)

with open(path("name.txt"), "r") as f:
    saved_name = f.read()

print("\nQ2: Name saved in name.txt:", saved_name)

# --- Q3: Write five lines, display them one by one ---
five_lines = [
    "Line 1: Python is fun.\n",
    "Line 2: File handling is useful.\n",
    "Line 3: Practice makes perfect.\n",
    "Line 4: Reading and writing files is easy.\n",
    "Line 5: Keep learning every day.\n",
]
with open(path("five_lines.txt"), "w") as f:
    f.writelines(five_lines)

print("\nQ3: Lines from five_lines.txt:")
with open(path("five_lines.txt"), "r") as f:
    for line in f:
        print(line.strip())

# --- Q4: Read an entire file and print its contents ---
with open(path("five_lines.txt"), "r") as f:
    whole_file = f.read()
print("\nQ4: Entire file content:")
print(whole_file)

# --- Q5: Read a file line by line using a loop ---
print("Q5: Reading line by line:")
with open(path("five_lines.txt"), "r") as f:
    for line_number, line in enumerate(f, start=1):
        print(f"{line_number}: {line.strip()}")

# --- Q6: Count total number of lines ---
with open(path("five_lines.txt"), "r") as f:
    total_lines = len(f.readlines())
print("\nQ6: Total lines:", total_lines)

# --- Q7: Count total number of words ---
with open(path("five_lines.txt"), "r") as f:
    text_content = f.read()
    total_words = len(text_content.split())
print("Q7: Total words:", total_words)

# --- Q8: Count total number of characters ---
with open(path("five_lines.txt"), "r") as f:
    total_chars = len(f.read())
print("Q8: Total characters:", total_chars)


# =========================================================
# PART 2: APPENDING & UPDATING FILES (9-14)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: APPENDING & UPDATING FILES")
print("=" * 50)

# --- Q9: Append a new line without deleting previous content ---
with open(path("hello.txt"), "a") as f:
    f.write("\nThis line was appended without deleting the original content.")

with open(path("hello.txt"), "r") as f:
    print("\nQ9: hello.txt after appending:")
    print(f.read())

# --- Q10: Continuously add notes to a file (simulated) ---
def add_note(note_text):
    with open(path("notes_demo.txt"), "a") as f:
        f.write(note_text + "\n")

# In real interactive use:
# while True:
#     note = input("Enter a note (or 'exit' to stop): ")
#     if note.lower() == "exit":
#         break
#     add_note(note)

sample_notes = ["Buy groceries", "Finish Python practice", "Call the doctor"]
for note in sample_notes:
    add_note(note)

print("\nQ10: notes_demo.txt after adding notes:")
with open(path("notes_demo.txt"), "r") as f:
    print(f.read())

# --- Q11: Replace every occurrence of a word in a file ---
with open(path("replace_demo.txt"), "w") as f:
    f.write("I like cats. Cats are wonderful pets. My cat sleeps a lot.")

def replace_word_in_file(filename, old_word, new_word):
    with open(filename, "r") as f:
        content = f.read()
    updated_content = content.replace(old_word, new_word)
    with open(filename, "w") as f:
        f.write(updated_content)

replace_word_in_file(path("replace_demo.txt"), "cat", "dog")
with open(path("replace_demo.txt"), "r") as f:
    print("\nQ11: After replacing 'cat' with 'dog':")
    print(f.read())

# --- Q12: Copy contents of one file into another ---
def copy_file(source, destination):
    with open(source, "r") as src, open(destination, "w") as dst:
        dst.write(src.read())

copy_file(path("hello.txt"), path("hello_copy.txt"))
print("\nQ12: Contents copied to hello_copy.txt:")
with open(path("hello_copy.txt"), "r") as f:
    print(f.read())

# --- Q13: Merge two text files into a third file ---
with open(path("file_a.txt"), "w") as f:
    f.write("Content from file A.\n")
with open(path("file_b.txt"), "w") as f:
    f.write("Content from file B.\n")

def merge_files(file1, file2, output_file):
    with open(output_file, "w") as out:
        for filename in (file1, file2):
            with open(filename, "r") as f:
                out.write(f.read())

merge_files(path("file_a.txt"), path("file_b.txt"), path("merged.txt"))
print("\nQ13: Merged file contents:")
with open(path("merged.txt"), "r") as f:
    print(f.read())

# --- Q14: Create a backup copy of a file ---
def backup_file(filename):
    backup_name = filename.replace(".txt", "_backup.txt")
    copy_file(filename, backup_name)
    return backup_name

backup_path = backup_file(path("hello.txt"))
print("Q14: Backup created at:", os.path.basename(backup_path))


# =========================================================
# PART 3: SEARCHING & PROCESSING FILES (15-20)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: SEARCHING & PROCESSING FILES")
print("=" * 50)

# Prepare a sample text file for searching/processing tasks
sample_text = """Python is a popular programming language.
Python is easy to learn and powerful.

It is widely used in data science, web development, and automation.
Many beginners choose Python as their first language.

"""
with open(path("sample_search.txt"), "w") as f:
    f.write(sample_text)

# --- Q15: Search for a word, show existence and count ---
def search_word_in_file(filename, target_word):
    with open(filename, "r") as f:
        content = f.read()
    count = content.lower().split().count(target_word.lower())
    # Using a simple word-boundary-aware count via split() comparison
    words = content.lower().replace(".", "").replace(",", "").split()
    occurrence_count = words.count(target_word.lower())
    exists = occurrence_count > 0
    return exists, occurrence_count

exists15, count15 = search_word_in_file(path("sample_search.txt"), "python")
print(f"\nQ15: 'python' exists: {exists15}, occurrences: {count15}")

# --- Q16: Longest line in a file ---
def longest_line(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return max(lines, key=len)

print("\nQ16: Longest line:", longest_line(path("sample_search.txt")))

# --- Q17: Shortest line in a file ---
def shortest_line(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    return min(lines, key=len)

print("Q17: Shortest line:", shortest_line(path("sample_search.txt")))

# --- Q18: Remove all blank lines from a file ---
def remove_blank_lines(filename, output_filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    non_blank_lines = [line for line in lines if line.strip() != ""]
    with open(output_filename, "w") as f:
        f.writelines(non_blank_lines)

remove_blank_lines(path("sample_search.txt"), path("no_blanks.txt"))
print("\nQ18: Contents after removing blank lines:")
with open(path("no_blanks.txt"), "r") as f:
    print(f.read())

# --- Q19: Display only lines containing a specific keyword ---
def find_lines_with_keyword(filename, keyword):
    with open(filename, "r") as f:
        matching_lines = [line.strip() for line in f if keyword.lower() in line.lower()]
    return matching_lines

print("Q19: Lines containing 'Python':")
for matched_line in find_lines_with_keyword(path("sample_search.txt"), "Python"):
    print(matched_line)

# --- Q20: Top 5 most frequently occurring words ---
def top_n_words(filename, n=5):
    with open(filename, "r") as f:
        content = f.read().lower()
    for punct in ".,!?;:\n":
        content = content.replace(punct, " ")
    words = content.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    sorted_words = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:n]

print("\nQ20: Top 5 most frequent words:")
for word, freq in top_n_words(path("sample_search.txt"), 5):
    print(f"{word}: {freq}")


# =========================================================
# PART 4: WORKING WITH MULTIPLE FILES (21-24)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: WORKING WITH MULTIPLE FILES")
print("=" * 50)

# --- Q21: Read three files, display combined contents ---
with open(path("file_1.txt"), "w") as f:
    f.write("This is file one.\n")
with open(path("file_2.txt"), "w") as f:
    f.write("This is file two.\n")
with open(path("file_3.txt"), "w") as f:
    f.write("This is file three.\n")

def combine_files(filenames):
    combined = ""
    for filename in filenames:
        with open(filename, "r") as f:
            combined += f.read()
    return combined

print("\nQ21: Combined contents of three files:")
print(combine_files([path("file_1.txt"), path("file_2.txt"), path("file_3.txt")]))

# --- Q22: Compare two files for identical content ---
def files_are_identical(file1, file2):
    with open(file1, "r") as f1, open(file2, "r") as f2:
        return f1.read() == f2.read()

# file_1.txt and file_2.txt have different content; hello.txt and hello_copy.txt should match
# (hello.txt was modified with an append after the copy, so let's create a true matching pair)
with open(path("match_a.txt"), "w") as f:
    f.write("Identical content for testing.")
with open(path("match_b.txt"), "w") as f:
    f.write("Identical content for testing.")

print("\nQ22: file_1.txt vs file_2.txt identical:",
      files_are_identical(path("file_1.txt"), path("file_2.txt")))
print("Q22: match_a.txt vs match_b.txt identical:",
      files_are_identical(path("match_a.txt"), path("match_b.txt")))

# --- Q23: Display all filenames inside a folder ---
print("\nQ23: Files inside practice_files folder:")
for filename in os.listdir(DATA_DIR):
    print(filename)

# --- Q24: Read every .txt file in a folder and display contents ---
print("\nQ24: Contents of every .txt file in the folder:")
for filename in os.listdir(DATA_DIR):
    if filename.endswith(".txt"):
        full_path = os.path.join(DATA_DIR, filename)
        with open(full_path, "r") as f:
            print(f"--- {filename} ---")
            print(f.read())


# =========================================================
# PART 5: FILE UTILITIES (25-27)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: FILE UTILITIES")
print("=" * 50)

# --- Q25: File size in bytes, KB, MB ---
def file_size_report(filename):
    size_bytes = os.path.getsize(filename)
    size_kb = size_bytes / 1024
    size_mb = size_kb / 1024
    return size_bytes, size_kb, size_mb

bytes_size, kb_size, mb_size = file_size_report(path("sample_search.txt"))
print("\nQ25: sample_search.txt size ->")
print(f"Bytes: {bytes_size}")
print(f"Kilobytes: {kb_size:.4f}")
print(f"Megabytes: {mb_size:.6f}")

# --- Q26: Rename an existing file ---
with open(path("old_name.txt"), "w") as f:
    f.write("This file will be renamed.")

old_file_path = path("old_name.txt")
new_file_path = path("new_name.txt")
os.rename(old_file_path, new_file_path)
print("\nQ26: File renamed. Now exists:", os.path.exists(new_file_path))

# --- Q27: Delete a file after confirming with the user ---
def delete_file_with_confirmation(filename, confirmed):
    """
    In real interactive use:
    confirm = input(f"Are you sure you want to delete {filename}? (yes/no): ")
    if confirm.lower() == 'yes':
        os.remove(filename)
        print("File deleted.")
    else:
        print("Deletion cancelled.")
    """
    if confirmed:
        os.remove(filename)
        return "File deleted."
    return "Deletion cancelled."

with open(path("to_delete.txt"), "w") as f:
    f.write("This file is about to be deleted.")

print("\nQ27:", delete_file_with_confirmation(path("to_delete.txt"), confirmed=True))
print("File still exists:", os.path.exists(path("to_delete.txt")))


# =========================================================
# PART 6: REAL-WORLD MINI PROJECTS (28-30)
# =========================================================

print("\n" + "=" * 50)
print("PART 6: REAL-WORLD MINI PROJECTS")
print("=" * 50)

# --- Q28: Notes Manager ---
class NotesManager:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()

    def add_note(self, note_text):
        with open(self.filename, "a") as f:
            f.write(note_text + "\n")

    def view_all_notes(self):
        with open(self.filename, "r") as f:
            return [line.strip() for line in f if line.strip()]

    def search_note(self, keyword):
        return [note for note in self.view_all_notes() if keyword.lower() in note.lower()]

    def delete_note(self, note_text):
        notes = self.view_all_notes()
        if note_text in notes:
            notes.remove(note_text)
            with open(self.filename, "w") as f:
                for note in notes:
                    f.write(note + "\n")
            return True
        return False

print("\nQ28: Notes Manager")
notes_manager = NotesManager(path("notes_manager.txt"))
notes_manager.add_note("Finish the file handling practice")
notes_manager.add_note("Review Python lists and dictionaries")
notes_manager.add_note("Prepare for the coding interview")
print("All notes:", notes_manager.view_all_notes())
print("Search 'interview':", notes_manager.search_note("interview"))
notes_manager.delete_note("Review Python lists and dictionaries")
print("After deleting a note:", notes_manager.view_all_notes())

# --- Q29: Student Record Manager ---
class StudentRecordManager:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()

    def _read_records(self):
        records = []
        with open(self.filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    roll, name, marks = line.split(",")
                    records.append({"roll": roll, "name": name, "marks": marks})
        return records

    def _write_records(self, records):
        with open(self.filename, "w") as f:
            for record in records:
                f.write(f"{record['roll']},{record['name']},{record['marks']}\n")

    def add_student(self, roll, name, marks):
        with open(self.filename, "a") as f:
            f.write(f"{roll},{name},{marks}\n")

    def view_all_students(self):
        return self._read_records()

    def search_by_roll(self, roll):
        for record in self._read_records():
            if record["roll"] == roll:
                return record
        return None

    def update_student(self, roll, new_name=None, new_marks=None):
        records = self._read_records()
        for record in records:
            if record["roll"] == roll:
                if new_name:
                    record["name"] = new_name
                if new_marks:
                    record["marks"] = new_marks
        self._write_records(records)

    def delete_student(self, roll):
        records = self._read_records()
        records = [r for r in records if r["roll"] != roll]
        self._write_records(records)

print("\nQ29: Student Record Manager")
student_manager = StudentRecordManager(path("students.txt"))
student_manager.add_student("R01", "Aarav", 85)
student_manager.add_student("R02", "Isha", 90)
student_manager.add_student("R03", "Vikram", 76)
print("All students:", student_manager.view_all_students())
print("Search R02:", student_manager.search_by_roll("R02"))
student_manager.update_student("R03", new_marks=82)
print("After updating R03's marks:", student_manager.search_by_roll("R03"))
student_manager.delete_student("R01")
print("After deleting R01:", student_manager.view_all_students())

# --- Q30: Expense Tracker (file-based) ---
class FileExpenseTracker:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(self.filename):
            open(self.filename, "w").close()

    def _read_expenses(self):
        expenses = []
        with open(self.filename, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    category, amount = line.split(",")
                    expenses.append({"category": category, "amount": float(amount)})
        return expenses

    def add_expense(self, category, amount):
        with open(self.filename, "a") as f:
            f.write(f"{category},{amount}\n")

    def view_all_expenses(self):
        return self._read_expenses()

    def total_expenses(self):
        return sum(e["amount"] for e in self._read_expenses())

    def highest_expense(self):
        expenses = self._read_expenses()
        return max(expenses, key=lambda e: e["amount"]) if expenses else None

    def lowest_expense(self):
        expenses = self._read_expenses()
        return min(expenses, key=lambda e: e["amount"]) if expenses else None

    def search_by_category(self, category):
        return [e for e in self._read_expenses() if e["category"].lower() == category.lower()]

    def generate_summary_report(self):
        expenses = self._read_expenses()
        if not expenses:
            return "No expenses recorded."
        total = sum(e["amount"] for e in expenses)
        highest = max(expenses, key=lambda e: e["amount"])
        lowest = min(expenses, key=lambda e: e["amount"])
        average = total / len(expenses)
        report = (
            f"Total expenses: {total:.2f}\n"
            f"Number of entries: {len(expenses)}\n"
            f"Average expense: {average:.2f}\n"
            f"Highest expense: {highest['category']} - {highest['amount']:.2f}\n"
            f"Lowest expense: {lowest['category']} - {lowest['amount']:.2f}"
        )
        return report

print("\nQ30: Expense Tracker")
expense_tracker = FileExpenseTracker(path("expenses.txt"))
expense_tracker.add_expense("Groceries", 1200)
expense_tracker.add_expense("Transport", 300)
expense_tracker.add_expense("Entertainment", 800)
expense_tracker.add_expense("Groceries", 450)
print("All expenses:", expense_tracker.view_all_expenses())
print("Total expenses:", expense_tracker.total_expenses())
print("Highest expense:", expense_tracker.highest_expense())
print("Lowest expense:", expense_tracker.lowest_expense())
print("Search 'Groceries':", expense_tracker.search_by_category("Groceries"))
print("\nSummary report:")
print(expense_tracker.generate_summary_report())

print("\n" + "=" * 50)
print(f"All demo files are stored in: {DATA_DIR}")
print("=" * 50)