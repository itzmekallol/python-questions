"""
main.py — imports functions from all three modules of the utilities package.

Q11: Demonstrates importing from a custom package.

Run with: python main.py
"""

from utilities.math_utils import square, is_prime
from utilities.string_utils import reverse_string, count_words
from utilities.file_utils import create_text_file, get_file_size

print("Q11: Using the utilities package")
print("Square of 7:", square(7))
print("Is 13 prime?", is_prime(13))
print("Reversed 'package':", reverse_string("package"))
print("Word count in 'this is a test sentence':", count_words("this is a test sentence"))

print(create_text_file("sample_output.txt", "Hello from the utilities package!"))
print("File size in bytes:", get_file_size("sample_output.txt"))
