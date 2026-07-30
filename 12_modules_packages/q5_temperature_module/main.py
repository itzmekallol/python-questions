"""
main.py — demonstrates three different import styles for temperature.py.

Q5:
  1. import module
  2. from module import function
  3. from module import *

Run with: python main.py
"""

# --- Style 1: import module ---
import temperature

print("Q5: Three import styles")
print("\nStyle 1 - 'import temperature':")
print("37C to F:", temperature.celsius_to_fahrenheit(37))

# --- Style 2: from module import function ---
from temperature import fahrenheit_to_celsius

print("\nStyle 2 - 'from temperature import fahrenheit_to_celsius':")
print("98.6F to C:", round(fahrenheit_to_celsius(98.6), 2))

# --- Style 3: from module import * ---
from temperature import *

print("\nStyle 3 - 'from temperature import *':")
print("0C to F:", celsius_to_fahrenheit(0))
print("32F to C:", fahrenheit_to_celsius(32))
