"""
Python Practice — Exception Handling (20 Questions)
Solutions with explanations.

Run this file with: python python_exception_handling_practice.py

Wherever input() would normally be used, sample fallback values (including
deliberately invalid ones, to demonstrate the error handling) are used
instead so the script runs end-to-end without manual entry. Real
input()-based versions are shown in comments so you can drop them into an
interactive session.
"""

import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# =========================================================
# PART 1: BASIC EXCEPTION HANDLING (1-5)
# =========================================================

print("=" * 50)
print("PART 1: BASIC EXCEPTION HANDLING")
print("=" * 50)

# --- Q1: Division, handle ZeroDivisionError ---
def safe_divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

print("\nQ1:")
print("10 / 2 ->", safe_divide(10, 2))
print("10 / 0 ->", safe_divide(10, 0))

# --- Q2: Handle invalid integer input ---
def get_valid_integer(value):
    try:
        return int(value)
    except ValueError:
        return "Error: Please enter a valid integer"

# real interactive version:
# user_input = input("Enter an integer: ")
print("\nQ2:")
print("'42' ->", get_valid_integer("42"))
print("'abc' ->", get_valid_integer("abc"))

# --- Q3: Handle invalid list index ---
numbers_list = [10, 20, 30, 40, 50]

def get_element_at_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range"

# index_input = int(input("Enter an index: "))
print("\nQ3:")
print("Index 2 ->", get_element_at_index(numbers_list, 2))
print("Index 10 ->", get_element_at_index(numbers_list, 10))

# --- Q4: Handle missing file ---
def read_file_safely(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' does not exist"

# filename_input = input("Enter a filename: ")
print("\nQ4:")
print(read_file_safely(path("does_not_exist.txt")))

# --- Q5: try / except / else / finally ---
def demonstrate_all_blocks(num1, num2):
    print(f"\nAttempting {num1} / {num2}")
    try:
        result = num1 / num2
    except ZeroDivisionError:
        print("except block: Division by zero caught")
    else:
        print(f"else block: Division succeeded, result = {result}")
    finally:
        print("finally block: This always runs, regardless of success or failure")

print("\nQ5:")
demonstrate_all_blocks(10, 2)   # triggers try + else + finally
demonstrate_all_blocks(10, 0)   # triggers try + except + finally


# =========================================================
# PART 2: MULTIPLE EXCEPTIONS (6-10)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: MULTIPLE EXCEPTIONS")
print("=" * 50)

# --- Q6: Separate except blocks for ValueError and ZeroDivisionError ---
def divide_with_specific_errors(num1_str, num2_str):
    try:
        num1 = int(num1_str)
        num2 = int(num2_str)
        return num1 / num2
    except ValueError:
        return "Error: Both inputs must be valid integers"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

print("\nQ6:")
print("'20', '4' ->", divide_with_specific_errors("20", "4"))
print("'20', '0' ->", divide_with_specific_errors("20", "0"))
print("'abc', '4' ->", divide_with_specific_errors("abc", "4"))

# --- Q7: Read a number from a file, divide by user value, handle all exceptions ---
with open(path("divisor_source.txt"), "w") as f:
    f.write("50")

def divide_number_from_file(filename, divisor_str):
    try:
        with open(filename, "r") as f:
            number_from_file = float(f.read().strip())
        divisor = float(divisor_str)
        return number_from_file / divisor
    except FileNotFoundError:
        return "Error: File not found"
    except ValueError:
        return "Error: File content or divisor is not a valid number"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# filename_input = input("Enter filename: ")
# divisor_input = input("Enter number to divide by: ")
print("\nQ7:")
print("Divide by '5' ->", divide_number_from_file(path("divisor_source.txt"), "5"))
print("Divide by '0' ->", divide_number_from_file(path("divisor_source.txt"), "0"))
print("Missing file ->", divide_number_from_file(path("missing_file.txt"), "5"))

# --- Q8: Calculator with exception-protected menu ---
def protected_calculator(choice, num1_str, num2_str):
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        return "Error: Please enter valid numbers"

    try:
        if choice == 1:
            return num1 + num2
        elif choice == 2:
            return num1 - num2
        elif choice == 3:
            return num1 * num2
        elif choice == 4:
            return num1 / num2
        else:
            return "Error: Invalid menu choice"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

print("\nQ8: Calculator")
print("Add 5 + 3 ->", protected_calculator(1, "5", "3"))
print("Divide 5 / 0 ->", protected_calculator(4, "5", "0"))
print("Invalid choice 9 ->", protected_calculator(9, "5", "3"))
print("Invalid numbers ->", protected_calculator(1, "five", "3"))

# --- Q9: Keep asking until valid input is provided (simulated) ---
def get_two_valid_numbers(simulated_inputs):
    """
    Real interactive version:

    while True:
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
            result = n1 / n2
            return result
        except ValueError:
            print("Invalid input, please enter numeric values.")
        except ZeroDivisionError:
            print("Cannot divide by zero, please try again.")

    Here we simulate a user who makes mistakes before entering valid data.
    simulated_inputs is a list of (num1_str, num2_str) attempts.
    """
    for attempt_num1, attempt_num2 in simulated_inputs:
        try:
            n1 = float(attempt_num1)
            n2 = float(attempt_num2)
            result = n1 / n2
            print(f"Success with ({attempt_num1}, {attempt_num2}) -> {result}")
            return result
        except ValueError:
            print(f"Attempt ({attempt_num1}, {attempt_num2}) failed: invalid input, retrying...")
        except ZeroDivisionError:
            print(f"Attempt ({attempt_num1}, {attempt_num2}) failed: division by zero, retrying...")
    return None

print("\nQ9:")
attempts = [("abc", "5"), ("10", "0"), ("10", "2")]
get_two_valid_numbers(attempts)

# --- Q10: Menu-driven program, every operation exception-protected ---
def safe_menu_operation(choice, value_str):
    try:
        value = float(value_str)
        if choice == 1:
            return f"Square root: {value ** 0.5}" if value >= 0 else "Error: Cannot take square root of a negative number"
        elif choice == 2:
            return f"Reciprocal: {1 / value}"
        elif choice == 3:
            return f"Square: {value ** 2}"
        else:
            return "Error: Invalid menu choice"
    except ValueError:
        return "Error: Please enter a valid number"
    except ZeroDivisionError:
        return "Error: Cannot compute reciprocal of zero"

print("\nQ10: Menu-driven program")
print("Choice 1, value '16' ->", safe_menu_operation(1, "16"))
print("Choice 2, value '0' ->", safe_menu_operation(2, "0"))
print("Choice 3, value 'abc' ->", safe_menu_operation(3, "abc"))
print("Choice 9, value '5' ->", safe_menu_operation(9, "5"))


# =========================================================
# PART 3: RAISING EXCEPTIONS (11-14)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: RAISING EXCEPTIONS")
print("=" * 50)

# --- Q11: withdraw() raises exceptions for invalid amounts ---
def withdraw(balance, amount):
    if amount < 0:
        raise ValueError("Withdrawal amount cannot be negative")
    if amount > balance:
        raise ValueError("Withdrawal amount exceeds available balance")
    return balance - amount

print("\nQ11:")
try:
    print("Withdraw 200 from 500 ->", withdraw(500, 200))
    print("Withdraw -50 from 500 ->", withdraw(500, -50))
except ValueError as e:
    print("Caught error:", e)

try:
    print("Withdraw 1000 from 500 ->", withdraw(500, 1000))
except ValueError as e:
    print("Caught error:", e)

# --- Q12: Validate age, raise exceptions ---
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age cannot be greater than 120")
    return f"Valid age: {age}"

print("\nQ12:")
for test_age in [25, -5, 150]:
    try:
        print(validate_age(test_age))
    except ValueError as e:
        print(f"Age {test_age} -> Caught error: {e}")

# --- Q13: Validate password, raise multiple exceptions ---
def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not any(c.isupper() for c in password):
        raise ValueError("Password must contain at least one uppercase letter")
    if not any(c.islower() for c in password):
        raise ValueError("Password must contain at least one lowercase letter")
    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain at least one digit")
    if not any(not c.isalnum() for c in password):
        raise ValueError("Password must contain at least one special character")
    return "Password is valid"

print("\nQ13:")
for test_password in ["short", "alllowercase1!", "NoDigitsHere!", "StrongPass1!"]:
    try:
        print(f"'{test_password}' ->", validate_password(test_password))
    except ValueError as e:
        print(f"'{test_password}' -> Caught error: {e}")

# --- Q14: Validate email format ---
import re

def validate_email(email):
    pattern = r"^[\w\.\-]+@[\w\-]+(\.[\w\-]+)*\.[a-zA-Z]{2,}$"
    if not re.match(pattern, email):
        raise ValueError(f"'{email}' is not a valid email format")
    return f"'{email}' is a valid email"

print("\nQ14:")
for test_email in ["user@example.com", "invalid-email", "another.user@domain.co.in"]:
    try:
        print(validate_email(test_email))
    except ValueError as e:
        print("Caught error:", e)


# =========================================================
# PART 4: CUSTOM EXCEPTIONS (15-17)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: CUSTOM EXCEPTIONS")
print("=" * 50)

# --- Q15: InsufficientBalanceError in a banking application ---
class InsufficientBalanceError(Exception):
    """Raised when a withdrawal amount exceeds the available balance."""
    pass

class SimpleBankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError(
                f"Cannot withdraw {amount}; available balance is {self.balance}"
            )
        self.balance -= amount
        return self.balance

print("\nQ15:")
account = SimpleBankAccount(1000)
try:
    print("Balance after withdrawing 400:", account.withdraw(400))
    print("Balance after withdrawing 800:", account.withdraw(800))
except InsufficientBalanceError as e:
    print("Caught InsufficientBalanceError:", e)

# --- Q16: InvalidAgeError ---
class InvalidAgeError(Exception):
    """Raised when age falls outside the valid range."""
    pass

def register_user(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Age {age} is outside the valid range (0-120)")
    return f"User registered successfully with age {age}"

print("\nQ16:")
for test_age in [30, -10, 200]:
    try:
        print(register_user(test_age))
    except InvalidAgeError as e:
        print("Caught InvalidAgeError:", e)

# --- Q17: InvalidMarksError ---
class InvalidMarksError(Exception):
    """Raised when marks fall outside the 0-100 range."""
    pass

def record_marks(marks):
    if marks < 0 or marks > 100:
        raise InvalidMarksError(f"Marks {marks} must be between 0 and 100")
    return f"Marks recorded: {marks}"

print("\nQ17:")
for test_marks in [85, -5, 150]:
    try:
        print(record_marks(test_marks))
    except InvalidMarksError as e:
        print("Caught InvalidMarksError:", e)


# =========================================================
# PART 5: REAL-WORLD MINI PROJECTS (18-20)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: REAL-WORLD MINI PROJECTS")
print("=" * 50)

# --- Q18: ATM System ---
class ATMSystem:
    def __init__(self, starting_balance=0):
        self.balance = starting_balance

    def deposit(self, amount_str):
        try:
            amount = float(amount_str)
            if amount < 0:
                raise ValueError("Deposit amount cannot be negative")
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        except ValueError as e:
            return f"Deposit failed: {e}"

    def withdraw(self, amount_str):
        try:
            amount = float(amount_str)
            if amount < 0:
                raise ValueError("Withdrawal amount cannot be negative")
            if amount > self.balance:
                raise InsufficientBalanceError(
                    f"Insufficient balance. Available: {self.balance}"
                )
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        except ValueError as e:
            return f"Withdrawal failed: {e}"
        except InsufficientBalanceError as e:
            return f"Withdrawal failed: {e}"

    def check_balance(self):
        return f"Current balance: {self.balance}"

    def menu_operation(self, choice, amount_str=None):
        try:
            if choice == 1:
                return self.deposit(amount_str)
            elif choice == 2:
                return self.withdraw(amount_str)
            elif choice == 3:
                return self.check_balance()
            else:
                raise ValueError("Invalid menu option")
        except ValueError as e:
            return f"Error: {e}"

print("\nQ18: ATM System")
atm = ATMSystem(starting_balance=2000)
print(atm.menu_operation(1, "500"))       # deposit
print(atm.menu_operation(2, "1000"))      # withdraw
print(atm.menu_operation(2, "5000"))      # insufficient balance
print(atm.menu_operation(1, "-100"))      # negative deposit
print(atm.menu_operation(3))              # check balance
print(atm.menu_operation(9, "100"))       # invalid menu option

# --- Q19: Student Management System ---
class DuplicateRollNumberError(Exception):
    """Raised when trying to add a student with an existing roll number."""
    pass

class StudentNotFoundError(Exception):
    """Raised when a student record cannot be found."""
    pass

class StudentManagementSystemSafe:
    def __init__(self):
        self.students = {}

    def add_student(self, roll_no, name, marks):
        try:
            if roll_no in self.students:
                raise DuplicateRollNumberError(f"Roll number {roll_no} already exists")
            if not (0 <= marks <= 100):
                raise InvalidMarksError(f"Marks {marks} must be between 0 and 100")
            self.students[roll_no] = {"name": name, "marks": marks}
            return f"Student {name} added successfully"
        except (DuplicateRollNumberError, InvalidMarksError) as e:
            return f"Error adding student: {e}"

    def get_student(self, roll_no):
        try:
            if roll_no not in self.students:
                raise StudentNotFoundError(f"No student found with roll number {roll_no}")
            return self.students[roll_no]
        except StudentNotFoundError as e:
            return f"Error: {e}"

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            return f"Error: File '{filename}' not found"

print("\nQ19: Student Management System")
student_system = StudentManagementSystemSafe()
print(student_system.add_student("R01", "Aarav", 88))
print(student_system.add_student("R01", "Someone Else", 70))  # duplicate roll number
print(student_system.add_student("R02", "Isha", 150))          # invalid marks
print(student_system.get_student("R01"))
print(student_system.get_student("R99"))                       # not found
print(student_system.load_from_file(path("nonexistent_records.txt")))

# --- Q20: Library Management System ---
class BookNotFoundError(Exception):
    """Raised when a requested book cannot be found."""
    pass

class DuplicateBookIDError(Exception):
    """Raised when trying to add a book with an existing ID."""
    pass

class LibraryManagementSystemSafe:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, title, author):
        try:
            if book_id in self.books:
                raise DuplicateBookIDError(f"Book ID {book_id} already exists")
            self.books[book_id] = {"title": title, "author": author}
            return f"Book '{title}' added successfully"
        except DuplicateBookIDError as e:
            return f"Error adding book: {e}"

    def get_book(self, book_id):
        try:
            if book_id not in self.books:
                raise BookNotFoundError(f"No book found with ID {book_id}")
            return self.books[book_id]
        except BookNotFoundError as e:
            return f"Error: {e}"

    def menu_operation(self, choice, book_id=None, title=None, author=None):
        try:
            if choice == 1:
                return self.add_book(book_id, title, author)
            elif choice == 2:
                return self.get_book(book_id)
            else:
                raise ValueError("Invalid menu choice")
        except ValueError as e:
            return f"Error: {e}"

    def load_records_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                return f.read()
        except FileNotFoundError:
            return f"Error: File '{filename}' not found"
        except PermissionError:
            return f"Error: No permission to read '{filename}'"

print("\nQ20: Library Management System")
library_system = LibraryManagementSystemSafe()
print(library_system.menu_operation(1, "B1", "The Hobbit", "J.R.R. Tolkien"))
print(library_system.menu_operation(1, "B1", "Duplicate Attempt", "Someone"))  # duplicate ID
print(library_system.menu_operation(2, "B1"))
print(library_system.menu_operation(2, "B99"))  # book not found
print(library_system.menu_operation(9))          # invalid menu choice
print(library_system.load_records_from_file(path("missing_library_data.txt")))

print("\n" + "=" * 50)
print("All demonstrations completed successfully.")
print("=" * 50)