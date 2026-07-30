"""
main.py — imports the calculator module and uses all four functions.

Run with: python main.py
"""

import calculator

print("Q1: Using the calculator module")
print("5 + 3 =", calculator.add(5, 3))
print("5 - 3 =", calculator.subtract(5, 3))
print("5 * 3 =", calculator.multiply(5, 3))
print("5 / 0 =", calculator.divide(5, 0))
print("10 / 2 =", calculator.divide(10, 2))
