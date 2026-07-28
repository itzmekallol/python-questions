"""
Python Practice — Functions (30 Questions)
Solutions with explanations.

Run this file with: python python_functions_practice.py
Wherever input() would normally be used, sample fallback values are used
instead so the script runs end-to-end without manual entry. Feel free to
swap in input() calls when experimenting interactively.
"""

# =========================================================
# PART 1: BASIC FUNCTIONS (1-10)
# =========================================================

print("=" * 50)
print("PART 1: BASIC FUNCTIONS")
print("=" * 50)

# --- Q1 ---
def greet():
    print("Welcome to Python Programming!")

print("\nQ1:")
greet()

# --- Q2 ---
def show_name(name):
    print(name)

print("\nQ2:")
show_name("Kallol")

# --- Q3 ---
def add(a, b):
    return a + b

print("\nQ3:", add(5, 3))

# --- Q4 ---
def subtract(a, b):
    return a - b

print("Q4:", subtract(5, 3))

# --- Q5 ---
def multiply(a, b):
    return a * b

print("Q5:", multiply(5, 3))

# --- Q6 ---
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

print("Q6:", divide(10, 2))
print("Q6 (div by zero):", divide(10, 0))

# --- Q7 ---
def square(number):
    return number ** 2

print("Q7:", square(6))

# --- Q8 ---
def cube(number):
    return number ** 3

print("Q8:", cube(3))

# --- Q9 ---
def is_even(number):
    return number % 2 == 0

print("Q9:", is_even(8))

# --- Q10 ---
def is_odd(number):
    return number % 2 != 0

print("Q10:", is_odd(7))


# =========================================================
# PART 2: FUNCTIONS WITH CONDITIONS (11-15)
# =========================================================

print("\n" + "=" * 50)
print("PART 2: FUNCTIONS WITH CONDITIONS")
print("=" * 50)

# --- Q11 ---
def largest(a, b):
    return a if a > b else b

print("\nQ11:", largest(45, 78))

# --- Q12 ---
def largest_of_three(a, b, c):
    return max(a, b, c)

print("Q12:", largest_of_three(12, 87, 45))

# --- Q13 ---
def number_type(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print("Q13:", number_type(-9))

# --- Q14 ---
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print("Q14:", is_leap_year(2028))

# --- Q15 ---
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print("Q15:", calculate_grade(84))


# =========================================================
# PART 3: FUNCTIONS WITH LOOPS (16-20)
# =========================================================

print("\n" + "=" * 50)
print("PART 3: FUNCTIONS WITH LOOPS")
print("=" * 50)

# --- Q16 ---
def factorial(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

print("\nQ16:", factorial(6))

# --- Q17 ---
def sum_to_n(number):
    total = 0
    for i in range(1, number + 1):
        total += i
    return total

print("Q17:", sum_to_n(50))

# --- Q18 ---
def reverse_number(number):
    temp = abs(number)
    reversed_num = 0
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
    return reversed_num if number >= 0 else -reversed_num

print("Q18:", reverse_number(12345))

# --- Q19 ---
def count_digits(number):
    temp = abs(number)
    if temp == 0:
        return 1
    count = 0
    while temp > 0:
        count += 1
        temp //= 10
    return count

print("Q19:", count_digits(987654))

# --- Q20 ---
def multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

print("Q20:")
multiplication_table(7)


# =========================================================
# PART 4: FUNCTION ARGUMENTS (21-24)
# =========================================================

print("\n" + "=" * 50)
print("PART 4: FUNCTION ARGUMENTS")
print("=" * 50)

# --- Q21: Default argument ---
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

print("\nQ21:")
greet_user()
greet_user("Kallol")

# --- Q22: *args ---
def sum_all(*args):
    return sum(args)

print("\nQ22:", sum_all(1, 2, 3, 4, 5))

# --- Q23: **kwargs ---
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("\nQ23:")
print_details(name="Kallol", age=20, city="Kolkata")

# --- Q24: Required + default + *args + **kwargs together ---
def demo_all_args(required_arg, default_arg="default value", *args, **kwargs):
    print("Required argument:", required_arg)
    print("Default argument:", default_arg)
    print("Extra positional args (*args):", args)
    print("Extra keyword args (**kwargs):", kwargs)

print("\nQ24:")
demo_all_args("must_provide", "custom_default", 1, 2, 3, city="Kolkata", country="India")


# =========================================================
# PART 5: LAMBDA FUNCTIONS (25-26)
# =========================================================

print("\n" + "=" * 50)
print("PART 5: LAMBDA FUNCTIONS")
print("=" * 50)

# --- Q25 ---
square_lambda = lambda number: number ** 2
print("\nQ25:", square_lambda(9))

# --- Q26 ---
larger_lambda = lambda a, b: a if a > b else b
print("Q26:", larger_lambda(23, 56))


# =========================================================
# PART 6: RECURSION (27-29)
# =========================================================

print("\n" + "=" * 50)
print("PART 6: RECURSION")
print("=" * 50)

# --- Q27 ---
def factorial_recursive(number):
    if number <= 1:
        return 1
    return number * factorial_recursive(number - 1)

print("\nQ27:", factorial_recursive(6))

# --- Q28 ---
def sum_to_n_recursive(number):
    if number <= 0:
        return 0
    return number + sum_to_n_recursive(number - 1)

print("Q28:", sum_to_n_recursive(50))

# --- Q29 ---
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print("Q29: 10th Fibonacci number =", fibonacci_recursive(10))


# =========================================================
# PART 7: MINI CHALLENGE (30)
# =========================================================

print("\n" + "=" * 50)
print("PART 7: MINI CHALLENGE - NUMBER UTILITY PROGRAM")
print("=" * 50)

def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def check_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def reverse_num(number):
    temp = abs(number)
    reversed_num = 0
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    return reversed_num if number >= 0 else -reversed_num

def digit_count(number):
    temp = abs(number)
    if temp == 0:
        return 1
    count = 0
    while temp > 0:
        count += 1
        temp //= 10
    return count

def factorial_util(number):
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result

def sum_1_to_n(number):
    return number * (number + 1) // 2

def number_utility_menu():
    """
    Displays a menu and calls the relevant function based on choice.
    In an interactive run this would loop with input(); here we
    simulate a few menu selections to demonstrate all features.
    """
    menu_text = """
    ----- Number Utility Program -----
    1. Check Even/Odd
    2. Check Prime
    3. Reverse Number
    4. Count Digits
    5. Calculate Factorial
    6. Calculate Sum from 1 to N
    7. Exit
    -----------------------------------
    """
    print(menu_text)

    # Simulated menu-driven run using sample inputs.
    # For real interactive use, replace the 'demo_choices' loop below with:
    #
    # while True:
    #     choice = int(input("Enter your choice (1-7): "))
    #     if choice == 7:
    #         print("Exiting program. Goodbye!")
    #         break
    #     num = int(input("Enter a number: "))
    #     if choice == 1:
    #         print("Result:", check_even_odd(num))
    #     elif choice == 2:
    #         print("Result:", "Prime" if check_prime(num) else "Not Prime")
    #     elif choice == 3:
    #         print("Result:", reverse_num(num))
    #     elif choice == 4:
    #         print("Result:", digit_count(num))
    #     elif choice == 5:
    #         print("Result:", factorial_util(num))
    #     elif choice == 6:
    #         print("Result:", sum_1_to_n(num))
    #     else:
    #         print("Invalid choice, try again.")

    demo_choices = [
        (1, 18),   # Check Even/Odd
        (2, 17),   # Check Prime
        (3, 4562), # Reverse Number
        (4, 98765),# Count Digits
        (5, 6),    # Factorial
        (6, 50),   # Sum from 1 to N
    ]

    for choice, num in demo_choices:
        if choice == 1:
            print(f"Choice 1 (Even/Odd) on {num} -> {check_even_odd(num)}")
        elif choice == 2:
            print(f"Choice 2 (Prime check) on {num} -> "
                  f"{'Prime' if check_prime(num) else 'Not Prime'}")
        elif choice == 3:
            print(f"Choice 3 (Reverse) on {num} -> {reverse_num(num)}")
        elif choice == 4:
            print(f"Choice 4 (Digit Count) on {num} -> {digit_count(num)}")
        elif choice == 5:
            print(f"Choice 5 (Factorial) on {num} -> {factorial_util(num)}")
        elif choice == 6:
            print(f"Choice 6 (Sum 1 to N) on {num} -> {sum_1_to_n(num)}")

    print("Choice 7 (Exit) -> Exiting program. Goodbye!")

number_utility_menu()
