"""
main.py — a menu-driven program built on top of the my_tools package.

Q14: Personal Utility Package.

Run with: python main.py

The real interactive menu loop is included as a comment inside
run_menu(); below it, a simulated run demonstrates every option so the
script executes end-to-end without needing manual entry.
"""

from my_tools.calculator import add, subtract, multiply, divide
from my_tools.converter import celsius_to_fahrenheit, km_to_miles, kg_to_pounds
from my_tools.password_generator import generate_password
from my_tools.validator import is_valid_email, is_valid_password


def run_menu():
    """
    Real interactive version:

    while True:
        print('''
        1. Calculator
        2. Unit Converter
        3. Password Generator
        4. Email/Password Validator
        5. Exit
        ''')
        choice = int(input("Choose an option: "))
        if choice == 5:
            print("Goodbye!")
            break
        elif choice == 1:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Operation (+, -, *, /): ")
            if op == "+":
                print(add(a, b))
            elif op == "-":
                print(subtract(a, b))
            elif op == "*":
                print(multiply(a, b))
            elif op == "/":
                print(divide(a, b))
        elif choice == 2:
            celsius = float(input("Enter Celsius value: "))
            print(celsius_to_fahrenheit(celsius))
        elif choice == 3:
            length = int(input("Password length: "))
            print(generate_password(length))
        elif choice == 4:
            email = input("Enter email: ")
            print("Valid email:", is_valid_email(email))
    """
    print("Q14: my_tools menu-driven demo")

    print("\n[Calculator] 15 + 7 =", add(15, 7))
    print("[Calculator] 15 / 0 =", divide(15, 0))

    print("\n[Converter] 30C to F:", celsius_to_fahrenheit(30))
    print("[Converter] 10km in miles:", round(km_to_miles(10), 2))
    print("[Converter] 70kg in pounds:", round(kg_to_pounds(70), 2))

    import random
    random.seed(7)  # seeded for reproducible demo output
    print("\n[Password Generator] New 10-char password:", generate_password(10))

    print("\n[Validator] 'user@example.com' valid email:", is_valid_email("user@example.com"))
    print("[Validator] 'bad-email' valid email:", is_valid_email("bad-email"))
    print("[Validator] 'StrongPass1!' valid password:", is_valid_password("StrongPass1!"))
    print("[Validator] 'weak' valid password:", is_valid_password("weak"))


run_menu()
