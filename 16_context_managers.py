"""
Python Practice — Context Managers (10 Questions)
Solutions with explanations.

Run this file with: python python_context_managers_practice.py

Rules followed throughout:
- `with` is used wherever appropriate instead of manual open/close.
- Both class-based (__enter__/__exit__) and function-based
  (contextlib.contextmanager) styles are demonstrated.
- contextlib is used where the questions call for a function-based
  context manager.
- Every context manager guarantees cleanup, including when an
  exception is raised inside the `with` block.

Demo files this script creates live in a "practice_files" folder next
to this script, so nothing clutters your main working directory.
"""

import os
import time
from contextlib import contextmanager

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# =========================================================
# PART 1: USING BUILT-IN CONTEXT MANAGERS (1-3)
# =========================================================

print("=" * 50)
print("PART 1: USING BUILT-IN CONTEXT MANAGERS")
print("=" * 50)

# --- Q1: Read a file with `with`, explain why it's better than manual close() ---
with open(path("sample.txt"), "w") as f:
    f.write("Context managers make resource handling safe and automatic.\n")
    f.write("They guarantee cleanup even when errors occur.\n")

print("\nQ1:")
with open(path("sample.txt"), "r") as f:
    contents = f.read()
print(contents)
print(
    "Why `with` is better than manual close(): the file object's __exit__ method "
    "runs automatically as soon as the block ends, even if an exception is raised "
    "inside it. With a manual open()/close() pair, an exception between the two "
    "calls would skip close() entirely (unless wrapped in try/finally), silently "
    "leaking the file handle. `with` removes that risk without any extra code."
)

# --- Q2: Copy one file into another using nested `with` statements ---
def copy_file_nested_with(source_path, destination_path):
    with open(source_path, "r") as source_file:
        with open(destination_path, "w") as destination_file:
            destination_file.write(source_file.read())

copy_file_nested_with(path("sample.txt"), path("sample_copy.txt"))
print("\nQ2: Copied file contents:")
with open(path("sample_copy.txt"), "r") as f:
    print(f.read())

# --- Q3: Count lines, words, characters using only `with` ---
def file_statistics(filename):
    with open(filename, "r") as f:
        content = f.read()
    total_lines = content.count("\n") + (1 if content and not content.endswith("\n") else 0)
    total_words = len(content.split())
    total_characters = len(content)
    return total_lines, total_words, total_characters

lines, words, chars = file_statistics(path("sample.txt"))
print("\nQ3:")
print("Total lines:", lines)
print("Total words:", words)
print("Total characters:", chars)


# =========================================================
# PART 2: CLASS-BASED CONTEXT MANAGERS (4-6)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: CLASS-BASED CONTEXT MANAGERS")
print("=" * 50)

# --- Q4: Class-based context manager printing Entering/Exiting Context ---
class SimpleContext:
    def __enter__(self):
        print("Entering Context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")
        return False  # do not suppress exceptions

print("\nQ4:")
with SimpleContext():
    print("Inside the with block")

# --- Q5: Timer context manager measuring execution time ---
class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.perf_counter()
        self.elapsed = self.end_time - self.start_time
        print(f"Elapsed time: {self.elapsed:.6f} seconds")
        return False

print("\nQ5:")
with Timer():
    total = sum(i ** 2 for i in range(200000))
print("Sum result:", total)

# --- Q6: Context manager that opens a file and logs open/close ---
class LoggingFileOpener:
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print(f"File opened: {self.filename}")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        print(f"File closed: {self.filename}")
        return False

print("\nQ6:")
with LoggingFileOpener(path("sample.txt"), "r") as f:
    first_line = f.readline().strip()
    print("First line read:", first_line)


# =========================================================
# PART 3: FUNCTION-BASED CONTEXT MANAGERS (7-8)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: FUNCTION-BASED CONTEXT MANAGERS")
print("=" * 50)

# --- Q7: @contextmanager printing Start / block / End ---
@contextmanager
def start_end_context():
    print("Start")
    yield
    print("End")

print("\nQ7:")
with start_end_context():
    print("Executing the block")

# --- Q8: Temporarily change the working directory, then restore it ---
@contextmanager
def change_directory(destination):
    original_directory = os.getcwd()
    os.chdir(destination)
    try:
        yield
    finally:
        os.chdir(original_directory)  # always restore, even if an error occurred

temp_dir = path("temp_working_dir")
os.makedirs(temp_dir, exist_ok=True)

print("\nQ8:")
print("Before:", os.getcwd())
with change_directory(temp_dir):
    print("Inside the with block:", os.getcwd())
print("After (restored):", os.getcwd())


# =========================================================
# PART 4: REAL-WORLD MINI PROJECTS (9-10)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: REAL-WORLD MINI PROJECTS")
print("=" * 50)

# --- Q9: Database Connection Simulator ---
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connected = False

    def __enter__(self):
        self.connected = True
        print(f"Connected to database '{self.db_name}'")
        return self

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected to the database")
        print(f"Executing query: {sql}")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"An error occurred during the database session: {exc_value}")
        self.connected = False
        print(f"Connection to '{self.db_name}' closed")
        return True  # suppress the exception after handling it, so the script continues

print("\nQ9: Database Connection Simulator")
print("-- Successful session --")
with DatabaseConnection("app_db") as db:
    db.query("SELECT * FROM users")

print("\n-- Session with an error --")
with DatabaseConnection("app_db") as db:
    db.query("SELECT * FROM orders")
    raise ValueError("Simulated query failure")
print("Program continues normally after the handled error")

# --- Q10: Transaction Manager ---
class TransactionManager:
    def __init__(self, account_name):
        self.account_name = account_name

    def __enter__(self):
        print(f"Transaction started for account '{self.account_name}'")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("All operations succeeded — committing transaction")
        else:
            print(f"Error detected ({exc_value}) — rolling back transaction")
        print(f"Transaction ended for account '{self.account_name}'")
        return True  # suppress the exception after rolling back

print("\nQ10: Transaction Manager")
print("-- Successful transaction --")
with TransactionManager("ACC1001") as txn:
    print("Depositing ₹5000")
    print("Withdrawing ₹2000")

print("\n-- Transaction with a failure --")
with TransactionManager("ACC1001") as txn:
    print("Depositing ₹1000")
    raise RuntimeError("Insufficient funds for withdrawal")
print("Program continues normally after the rolled-back transaction")

print("\n" + "=" * 50)
print(f"Demo files are stored in: {DATA_DIR}")
print("=" * 50)