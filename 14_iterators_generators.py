"""
Python Practice — Iterators & Generators (20 Questions)
Solutions with explanations.

Run this file with: python python_iterators_generators_practice.py

Rules followed throughout:
- No external libraries (only Python's standard library, e.g. csv).
- `yield` is used for every generator.
- Comments call out the iterable vs. iterator vs. generator distinction
  where it matters.
- Code favors memory efficiency: values are produced lazily one at a
  time instead of building large lists in memory up front.

This script creates a couple of small demo files (a log file and a CSV
file) inside a "practice_files" folder next to this script, so the
real-world mini projects have something genuine to stream through.
"""

import csv
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# =========================================================
# PART 1: ITERATORS (1-8)
# =========================================================

print("=" * 50)
print("PART 1: ITERATORS")
print("=" * 50)

# --- Q1: Manual iteration over a list using iter() and next() ---
# A list is an ITERABLE (it has __iter__), but not itself an ITERATOR.
# iter() asks the list for an ITERATOR object, which is what next() advances.
numbers = [10, 20, 30, 40, 50]
number_iterator = iter(numbers)

print("\nQ1:")
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
print(next(number_iterator))
# A sixth next() call here would raise StopIteration, since the iterator is exhausted.

# --- Q2: Manual iteration over a tuple ---
colors = ("red", "green", "blue")
color_iterator = iter(colors)

print("\nQ2:")
print(next(color_iterator))
print(next(color_iterator))
print(next(color_iterator))

# --- Q3: Manual iteration over dictionary keys ---
person = {"name": "Kallol", "age": 20, "city": "Kolkata"}
key_iterator = iter(person.keys())

print("\nQ3:")
print(next(key_iterator))
print(next(key_iterator))
print(next(key_iterator))

# --- Q4: Print each character of a string using an iterator ---
word = "Python"
char_iterator = iter(word)

print("\nQ4:")
try:
    while True:
        print(next(char_iterator))
except StopIteration:
    pass  # the iterator is exhausted, so we stop the loop cleanly

# --- Q5: Custom iterator class returning numbers 1 to N ---
class NumberRange:
    """A custom ITERATOR: it defines both __iter__ and __next__."""

    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

print("\nQ5:")
for num in NumberRange(5):
    print(num)

# --- Q6: Custom iterator returning only even numbers ---
class EvenNumberRange:
    def __init__(self, n):
        self.n = n
        self.current = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 2
        return value

print("\nQ6:")
for num in EvenNumberRange(10):
    print(num)

# --- Q7: Custom iterator for a multiplication table ---
class MultiplicationTable:
    def __init__(self, number, up_to=10):
        self.number = number
        self.up_to = up_to
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.up_to:
            raise StopIteration
        result = self.number * self.current
        self.current += 1
        return f"{self.number} x {self.current - 1} = {result}"

print("\nQ7:")
for line in MultiplicationTable(7):
    print(line)

# --- Q8: Custom iterator through a list in reverse order ---
class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value

print("\nQ8:")
for item in ReverseListIterator([1, 2, 3, 4, 5]):
    print(item)


# =========================================================
# PART 2: GENERATOR FUNCTIONS (9-14)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: GENERATOR FUNCTIONS")
print("=" * 50)

# --- Q9: Generator yielding numbers 1 to N ---
# A generator function is automatically both an ITERABLE and an ITERATOR:
# calling it returns a generator object that supports next().
def numbers_up_to(n):
    for i in range(1, n + 1):
        yield i

print("\nQ9:")
for num in numbers_up_to(5):
    print(num)

# --- Q10: Generator yielding only even numbers up to N ---
def even_numbers_up_to(n):
    for i in range(2, n + 1, 2):
        yield i

print("\nQ10:")
for num in even_numbers_up_to(10):
    print(num)

# --- Q11: Generator yielding the Fibonacci sequence ---
def fibonacci_sequence(terms):
    a, b = 0, 1
    count = 0
    while count < terms:
        yield a
        a, b = b, a + b
        count += 1

print("\nQ11: First 10 Fibonacci numbers")
for num in fibonacci_sequence(10):
    print(num, end=" ")
print()

# --- Q12: Generator yielding a multiplication table ---
def multiplication_table_gen(number, up_to=10):
    for i in range(1, up_to + 1):
        yield f"{number} x {i} = {number * i}"

print("\nQ12:")
for line in multiplication_table_gen(9):
    print(line)

# --- Q13: Generator yielding each word from a sentence ---
def word_generator(sentence):
    for word in sentence.split():
        yield word

print("\nQ13:")
for word in word_generator("Generators are memory efficient in Python"):
    print(word)

# --- Q14: Generator yielding one line at a time from a text file ---
with open(path("sample_log.txt"), "w") as f:
    f.write(
        "2026-07-29 09:00:01 INFO Server started\n"
        "2026-07-29 09:01:15 INFO User logged in\n"
        "2026-07-29 09:02:47 ERROR Database connection failed\n"
        "2026-07-29 09:03:02 INFO Retry successful\n"
        "2026-07-29 09:05:30 WARNING High memory usage\n"
        "2026-07-29 09:07:11 ERROR Timeout while processing request\n"
    )

def read_lines_lazily(filename):
    """
    Reading a file with `for line in f` is already lazy (the file object
    is itself an iterator), but wrapping it in a generator makes the
    lazy, line-at-a-time contract explicit and reusable.
    """
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()

print("\nQ14:")
for line in read_lines_lazily(path("sample_log.txt")):
    print(line)


# =========================================================
# PART 3: GENERATOR EXPRESSIONS (15-16)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: GENERATOR EXPRESSIONS")
print("=" * 50)

# --- Q15: Generator expression for squares of 1-100 ---
# Note the () instead of [] — this builds a generator, not a list, so the
# 100 squares are never all held in memory at once.
squares_gen = (n ** 2 for n in range(1, 101))
print("\nQ15: First 10 squares (from a lazy generator expression):")
for i, square in enumerate(squares_gen):
    if i >= 10:
        break
    print(square, end=" ")
print("...")

# --- Q16: Generator expression filtering primes from a list ---
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

number_pool = [4, 7, 9, 11, 15, 17, 20, 23, 29, 30]
primes_gen = (n for n in number_pool if is_prime(n))
print("\nQ16: Prime numbers from the list:")
for prime in primes_gen:
    print(prime, end=" ")
print()


# =========================================================
# PART 4: ADVANCED ITERATORS & GENERATORS (17-18)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: ADVANCED ITERATORS & GENERATORS")
print("=" * 50)

# --- Q17: Infinite generator of natural numbers, stopped by the caller ---
def natural_numbers():
    n = 1
    while True:  # infinite - the generator never runs out on its own
        yield n
        n += 1

# stop_after = int(input("How many natural numbers should be printed? "))
stop_after = 8  # sample value
print(f"\nQ17: First {stop_after} natural numbers from an infinite generator")
nat_gen = natural_numbers()
for _ in range(stop_after):
    print(next(nat_gen), end=" ")
print()

# --- Q18: Custom iterator that cycles through days of the week forever ---
class DayCycler:
    """A custom ITERATOR that never raises StopIteration on its own —
    it wraps back to Monday after Sunday, forever."""

    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def __init__(self):
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        day = self.DAYS[self.index]
        self.index = (self.index + 1) % len(self.DAYS)
        return day

print("\nQ18: Cycling through 10 days (more than one full week):")
day_cycler = DayCycler()
for _ in range(10):
    print(next(day_cycler))


# =========================================================
# PART 5: REAL-WORLD MINI PROJECTS (19-20)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: REAL-WORLD MINI PROJECTS")
print("=" * 50)

# --- Q19: Log File Reader ---
def log_line_generator(filename):
    """Lazily yields one stripped line at a time from a log file."""
    with open(filename, "r") as f:
        for line in f:
            stripped = line.strip()
            if stripped:  # skip blank lines
                yield stripped

def search_log(filename, keyword):
    """
    Streams through the log file lazily (never loading the whole file
    into memory) and reports matches for the given keyword.
    """
    matching_lines = []
    match_count = 0
    for line in log_line_generator(filename):
        if keyword.lower() in line.lower():
            matching_lines.append(line)
            match_count += 1
    return matching_lines, match_count

print("\nQ19: Log File Reader")
matches, total_matches = search_log(path("sample_log.txt"), "ERROR")
print(f"Found {total_matches} line(s) containing 'ERROR':")
for line in matches:
    print(line)

# --- Q20: CSV Data Streamer ---
with open(path("employees.csv"), "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "department", "salary"])
    writer.writerow(["Ananya", "Engineering", "75000"])
    writer.writerow(["Rohan", "Marketing", "48000"])
    writer.writerow([])  # intentional blank row to demonstrate skipping
    writer.writerow(["Priya", "Engineering", "82000"])
    writer.writerow(["Vikram", "Sales", "39000"])

def csv_row_generator(filename):
    """Lazily yields one row (as a dict) at a time from a CSV file, skipping blank rows."""
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if any(value.strip() for value in row.values() if value is not None):
                yield row

def stream_csv_with_filter(filename, min_salary):
    """
    Streams the CSV lazily, counts total rows processed, and filters
    rows where salary exceeds min_salary.
    """
    total_rows = 0
    filtered_rows = []
    for row in csv_row_generator(filename):
        total_rows += 1
        if int(row["salary"]) > min_salary:
            filtered_rows.append(row)
    return filtered_rows, total_rows

print("\nQ20: CSV Data Streamer")
high_earners, rows_processed = stream_csv_with_filter(path("employees.csv"), 50000)
print(f"Total rows processed (blank rows skipped): {rows_processed}")
print("Employees with salary > 50000:")
for employee in high_earners:
    print(f"{employee['name']} - {employee['department']} - ₹{employee['salary']}")

print("\n" + "=" * 50)
print(f"Demo files are stored in: {DATA_DIR}")
print("=" * 50)