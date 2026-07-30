"""
Python Practice — Decorators (15 Questions)
Solutions with explanations.

Run this file with: python python_decorators_practice.py

Rules followed throughout:
- Every decorator is hand-built (no third-party libraries).
- functools.wraps is used wherever a decorator wraps a function, so
  __name__, __doc__, etc. are preserved on the decorated function.
- Original function behavior (return value, arguments) is kept intact
  unless a question specifically asks for different behavior (e.g. Q9
  only prints the return value in addition to returning it normally).

Q8 and Q15's @log_execution write to a real log file inside a
"practice_files" folder next to this script, so nothing clutters your
main working directory.
"""

import functools
import time
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


# =========================================================
# PART 1: BASIC DECORATORS (1-5)
# =========================================================

print("=" * 50)
print("PART 1: BASIC DECORATORS")
print("=" * 50)

# --- Q1: Print "Function Started" before executing ---
def print_start(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Function Started")
        return func(*args, **kwargs)
    return wrapper

@print_start
def greet(name):
    print(f"Hello, {name}!")

print("\nQ1:")
greet("Kallol")

# --- Q2: Also print "Function Finished" after executing ---
def print_start_and_finish(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Function Started")
        result = func(*args, **kwargs)
        print("Function Finished")
        return result
    return wrapper

@print_start_and_finish
def greet2(name):
    print(f"Hello, {name}!")

print("\nQ2:")
greet2("Isha")

# --- Q3: Print function name and arguments before calling ---
def print_call_details(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@print_call_details
def add(a, b):
    return a + b

print("\nQ3:")
print("Result:", add(5, 3))

# --- Q4: Count how many times a function has been called ---
def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"'{func.__name__}' has been called {wrapper.call_count} time(s)")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def say_hello():
    print("Hello!")

print("\nQ4:")
say_hello()
say_hello()
say_hello()

# --- Q5: Measure and display execution time ---
def measure_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"'{func.__name__}' executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@measure_time
def slow_square(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

print("\nQ5:")
print("Result:", slow_square(100000))


# =========================================================
# PART 2: DECORATORS WITH ARGUMENTS (6-9)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: DECORATORS WITH ARGUMENTS")
print("=" * 50)

# --- Q6: Decorator factory that accepts a message argument ---
def with_message(message):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@with_message("Starting the calculation...")
def multiply(a, b):
    return a * b

print("\nQ6:")
print("Result:", multiply(6, 7))

# --- Q7: Decorator that repeats a function N times ---
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")
    return "done"

print("\nQ7:")
outcomes = say_hi()
print("Return values from each call:", outcomes)

# --- Q8: Decorator that logs every function call to a text file ---
def log_to_file(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] Called '{func.__name__}' with args={args}, kwargs={kwargs}\n"
        with open(path("function_calls.log"), "a") as f:
            f.write(log_line)
        return func(*args, **kwargs)
    return wrapper

@log_to_file
def divide(a, b):
    return a / b

print("\nQ8:")
print("Result:", divide(10, 2))
print("Result:", divide(20, 4))
print("Log file contents:")
with open(path("function_calls.log"), "r") as f:
    print(f.read())

# --- Q9: Decorator that prints the return value ---
def print_return_value(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"'{func.__name__}' returned: {result}")
        return result
    return wrapper

@print_return_value
def square(n):
    return n ** 2

print("\nQ9:")
value = square(9)  # the print happens inside the decorator; value is still the real return


# =========================================================
# PART 3: PRACTICAL DECORATORS (10-12)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: PRACTICAL DECORATORS")
print("=" * 50)

# --- Q10: Only execute if the user is logged in (simulated) ---
is_logged_in = True  # simulated login state; flip to False to see it blocked

def require_login_simple(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not is_logged_in:
            print("Access denied: please log in first")
            return None
        return func(*args, **kwargs)
    return wrapper

@require_login_simple
def view_dashboard():
    print("Welcome to your dashboard!")

print("\nQ10:")
view_dashboard()
is_logged_in = False
view_dashboard()
is_logged_in = True  # reset for later examples

# --- Q11: Validate arguments (reject negatives, reject empty strings) ---
def validate_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Negative numbers are not allowed: {arg}")
            if isinstance(arg, str) and arg.strip() == "":
                raise ValueError("Empty strings are not allowed")
        return func(*args, **kwargs)
    return wrapper

@validate_arguments
def create_profile(name, age):
    return f"Profile created for {name}, age {age}"

print("\nQ11:")
print(create_profile("Ravi", 25))
try:
    create_profile("", 25)
except ValueError as e:
    print("Caught error:", e)
try:
    create_profile("Ravi", -5)
except ValueError as e:
    print("Caught error:", e)

# --- Q12: Caching (memoization) decorator ---
def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        print(f"Cache miss for {args}, calculating...")
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def slow_fibonacci(n):
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

print("\nQ12:")
print("fibonacci(10) =", slow_fibonacci(10))
print("fibonacci(10) again =", slow_fibonacci(10))  # should hit the cache directly


# =========================================================
# PART 4: ADVANCED DECORATORS (13-14)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: ADVANCED DECORATORS")
print("=" * 50)

# --- Q13: Class-based decorator counting executions ---
class CountCalls:
    """A decorator implemented as a class instead of a function.
    __call__ makes instances of this class usable as @CountCalls."""

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"'{self.func.__name__}' has been executed {self.calls} time(s)")
        return self.func(*args, **kwargs)

@CountCalls
def process_order():
    print("Processing order...")

print("\nQ13:")
process_order()
process_order()

# --- Q14: Decorator that works on class methods ---
def log_method_call(method):
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        print(f"Calling method '{method.__name__}' on {self.__class__.__name__} "
              f"with args={args}")
        return method(self, *args, **kwargs)
    return wrapper

class Calculator:
    @log_method_call
    def add(self, a, b):
        return a + b

    @log_method_call
    def subtract(self, a, b):
        return a - b

print("\nQ14:")
calc = Calculator()
print("Result:", calc.add(10, 5))
print("Result:", calc.subtract(10, 5))


# =========================================================
# PART 5: REAL-WORLD MINI PROJECT (15)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: PROFESSIONAL LOGGING & VALIDATION SYSTEM")
print("=" * 50)

# --- Q15: log_execution, require_login, validate_input, cache_result ---

def log_execution(func):
    """Logs function name, arguments, return value, and execution time to a file."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_line = (
            f"[{timestamp}] '{func.__name__}' args={args} kwargs={kwargs} "
            f"-> returned {result!r} in {duration:.6f}s\n"
        )
        with open(path("app.log"), "a") as f:
            f.write(log_line)
        return result
    return wrapper

# Simulated authentication state for require_login
current_user_authenticated = True

def require_login(func):
    """Allows execution only if the (simulated) user is authenticated."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user_authenticated:
            raise PermissionError("Access denied: user is not authenticated")
        return func(*args, **kwargs)
    return wrapper

def validate_input(*validators):
    """
    Decorator factory: validators is a tuple of functions, one per
    positional argument, each returning True if that argument is valid.

    Example: @validate_input(lambda x: x > 0, lambda x: x != "")
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for value, validator in zip(args, validators):
                if not validator(value):
                    raise ValueError(f"Invalid argument: {value!r} failed validation")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def cache_result(func):
    """Caches results for repeated calls with the same arguments."""
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper

# --- Demonstrating all four decorators together ---
@log_execution
@require_login
@validate_input(lambda salary: salary > 0, lambda bonus_pct: 0 <= bonus_pct <= 100)
@cache_result
def calculate_annual_pay(salary, bonus_pct):
    return salary + (salary * bonus_pct / 100)

print("\nQ15: Professional Logging & Validation System")
print("Annual pay:", calculate_annual_pay(600000, 10))
print("Annual pay (same args, should hit cache internally):", calculate_annual_pay(600000, 10))

try:
    calculate_annual_pay(-500, 10)  # fails validate_input
except ValueError as e:
    print("Caught validation error:", e)

current_user_authenticated = False
try:
    calculate_annual_pay(600000, 10)  # fails require_login
except PermissionError as e:
    print("Caught permission error:", e)
current_user_authenticated = True

print("\napp.log contents:")
with open(path("app.log"), "r") as f:
    print(f.read())

print("=" * 50)
print(f"Log files are stored in: {DATA_DIR}")
print("=" * 50)