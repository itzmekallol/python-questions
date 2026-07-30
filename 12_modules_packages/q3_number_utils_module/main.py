"""
main.py — imports only the required functions from number_utils.

Q3: Demonstrates a selective import (not the whole module).

Run with: python main.py
"""

from number_utils import is_prime, reverse_number, count_digits

print("Q3: Using selected functions from number_utils")
print("Is 17 prime?", is_prime(17))
print("Is 20 prime?", is_prime(20))
print("Reverse of 12345:", reverse_number(12345))
print("Digit count of 987654:", count_digits(987654))
